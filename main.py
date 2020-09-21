import os
import argparse
from data.dataset import Dataset

######################################   ASIGN VARIABLES   ######################################

PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
TRANSACTIONS = os.path.join(PATH, 'txs.json')
BLOCKS = os.path.join(PATH, 'blocks.json')
CONTROL_TIME=False
SHOW_PLOTS=False
PRICE=True
TEST=True

######################################   RUN   ######################################

if __name__ == "__main__":
    #The parameters can be introduced by the user
    parser = argparse.ArgumentParser(description='Pipeline execution')
    parser.add_argument('-p', '--path', default=PATH, help='Absolute path of the .json files')
    parser.add_argument('-t', '--transactions', default=TRANSACTIONS, help='Add the name of the txs.json file to the absolute path')
    parser.add_argument('-b', '--blocks', default=BLOCKS, help='Add the name of the blocks.json file to the absolute path')
    parser.add_argument('-ctrl', '--control_time', default= CONTROL_TIME, help='Control the time to parse the .json files by passing True or False')
    parser.add_argument('-plt', '--plot', default=SHOW_PLOTS, help='To show interactive plots')
    parser.add_argument('-pr', '--price', default=PRICE, help='To show bitcoin current price')
    parser.add_argument('-t', '--test', default=TEST, help='To activate test')
    args = parser.parse_args()


    data = Dataset(args.transactions, args.blocks, args.control_time, args.plot)
    trans, blocks = data.create_dataset()
    data.vals_trans_blocks(trans)
    data.num_transactions_hourly(blocks)
    data.num_trans(blocks)
    data.time_between_blocks(blocks)
    data.avg_size_hourly(blocks)
