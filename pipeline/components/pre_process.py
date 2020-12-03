import argparse

## may be these are public function so DS can use them while working on the notebooks
def _pre_process(train_location, test_location):
    '''Pre Process Data - For example check for NULL data in the set or we have a nuber for boolean column etc'''
    print(f'Print train and test location {train_location} {test_location}')
    return 'success'
     
if __name__ == '__main__':
     print('Preprocessing data...')
     parser = argparse.ArgumentParser()
     parser.add_argument('--train_location')
     parser.add_argument('--test_location')
     args = parser.parse_args()
     _pre_process(args.train_location, args.test_location)