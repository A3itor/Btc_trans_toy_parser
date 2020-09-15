import json
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


######################################   DEFINE CLASSES   ######################################


class Dataset:
    """
    This is a class for parsing two .json files containing bitcoin transactions data.

    Attributes:
        transactions (str): A path to a folder that contains the txs.json file.
        blocks (str): A path to a folder that contains the blocks.json file.
    """

    def __init__(self, transactions, blocks, ctrl_time, show_plots):
        """
        The constructor for Dataset class.

        Parameters:
            transactions (str): A path to a folder that contains the txs.json file.
            blocks (str): A path to a folder that contains the blocks.json file.
        """

        self.trans = transactions
        self.blocks = blocks
        self.ctrl_time = ctrl_time
        self.show_plots = show_plots

    def create_dataset(self):
        """
        The function to deserialize the .json files and store them into two lists of dictionaries.

        Returns:
            trans, blocks (lst,lst): Two lists of dictionaries containing data from bitcoin transactions as well as blocks.
        """

        start = time.time()
        trans = []
        with open(self.trans) as txs:
            for tx in txs:
                t = json.loads(tx)
                trans.append(t)
        end = time.time()
        if self.ctrl_time:
            print("\nTime to load txs.json: {} seconds".format(end - start))

        start = time.time()
        blocks = []
        with open(self.blocks) as blks:
            for blk in blks:
                b = json.loads(blk)
                blocks.append(b)
        end = time.time()
        if self.ctrl_time:
            print("\nTime to load blocks.json: {} seconds".format(end - start))
        return trans, blocks


    def num_trans(self, blocks):
        """
        The function to calculate the number of transactions per block.

        Parameters:
            blocks (lst): A list of dictionaries containing data about bitcoin blocks.

        Returns:
            A dictionary containing the number of transactions per block.
        """

        n_trans = {}
        for num, block in enumerate(blocks):
            n_trans["block_" + str(num + 1)] = block["nTx"]
        print("\nNumber of transactions per block:\n{}".format(n_trans))
        if self.show_plots:
            x = [e for e in range(len(n_trans.values()))]
            y = [v for v in n_trans.values()]

            ticks = np.arange(1, len(n_trans.values()) + 1, 1)
            fig, ax = plt.subplots()
            width = 0.7
            ax.set_xticks(ticks)
            ax.set_xticklabels(x)
            ax.set_yticklabels(y)
            ax.bar(ticks, y, width, color='Red')

            plt.show()
        return n_trans


    def vals_trans_blocks(self, trans):
        """
        The function to calculate the transactions total value per block.

        Parameters:
            trans (lst): A list of dictionaries containing data about bitcoin transactions.

        Returns:
            trans_vals_blcks (dict): A dictionary containing the transactions total value per block.
        """

        trans_vals_blcks = {}
        block = 0
        value = 0
        for n, tr in enumerate(trans):
            if n == 0:
                block = tr['blockhash']
            for e in tr["vout"]:
                if block != tr['blockhash']:
                    trans_vals_blcks["Hash_id " + block] = value
                    value = 0
                    block = tr['blockhash']
                else:
                    value += e["value"]
        print("\nTransactions total value per block:\n{}".format(trans_vals_blcks))
        return trans_vals_blcks


    def time_between_blocks(self, blocks):
        """
        The function to calculate the time between blocks.

        Parameters:
            blocks (lst): A list of dictionaries containing data about bitcoin blocks.

        Returns:
            dic (dict): A dictionary containing the time between blocks.
        """

        # Sort time
        lst = []
        for block in blocks:
            lst.append(block['time'])
        lst.sort()
        # Calculate T difference
        dic = {}
        count = 0
        for k, v in zip(lst, lst[1:]):
            d = v - k
            d = datetime.fromtimestamp(d).strftime("%-Mm:%Ss")
            dic.update({"{} and {}".format(
                str(count), str(count + 1)): d})
            count += 1
        print("\nTime difference between blocks:\n{}".format(dic))
        return dic


    def avg_size_hourly(self, blocks):
        """
        The function to calculate the average size of the block in one hour (from all the timestamps).

        Parameters:
            blocks (lst): A list of dictionaries containing data about bitcoin blocks.

        Returns:
            np.mean(avg) (float): A scalar of the mean of the average size of the block in one hour.
        """

        # Convert from timestamp
        time = []
        for block in blocks:
            h = datetime.fromtimestamp(block['time']).strftime('%d-%H')
            if h not in time: time.append(h)
        # Calculate average
        avg = []
        for t in time:
            avg.append(np.mean(
                [block['size'] for block in blocks if t == datetime.fromtimestamp(block['time']).strftime('%d-%H')]))
        print("\nAverage size of block per hour:\n{}".format(np.mean(avg)))
        return np.mean(avg)


    def num_transactions_hourly(self, blocks):
        """
        The function to calculate the number of transactions per hour, spread among several days.

        Parameters:
            blocks (lst): A list of dictionaries containing data about bitcoin blocks.

        Returns:
            num_trans (lst): A list containing the number of transactions per hour, spread among several days.
        """
        # Convert from timestamp
        time = []
        for block in blocks:
            t = datetime.fromtimestamp(block['time']).strftime('%d-%H')
            if t not in time: time.append(t)
        # Calculate total transactions hourly
        num_trans = []
        for t in time:
            num_trans.append(
                np.sum([i['nTx'] for i in blocks if t == datetime.fromtimestamp(i['time']).strftime('%d-%H')]))
        print("\nNumber of transactions per hour (27 hours splitted in two days):\n{}".format(num_trans))
        return num_trans


######################################   RUN   ######################################


if __name__ == "__main__":
    PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
    TRANSACTIONS = os.path.join(PATH, 'txs.json')
    BLOCKS = os.path.join(PATH, 'blocks.json')
    CONTROL_TIME = False
    SHOW_PLOTS = False

    data = Dataset(transactions=TRANSACTIONS, blocks=BLOCKS, ctrl_time=CONTROL_TIME, show_plots=SHOW_PLOTS)
    trans, blocks = data.create_dataset()
    data.vals_trans_blocks(trans)
    data.num_transactions_hourly(blocks)
    data.num_trans(blocks)
    data.time_between_blocks(blocks)
    data.avg_size_hourly(blocks)
