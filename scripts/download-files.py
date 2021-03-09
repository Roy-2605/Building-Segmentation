import wget

TRAIN_TIER_1 = 'https://drivendata-public-assets.s3.amazonaws.com/train_tier_1.tgz'
TRAIN_TIER_2 = 'https://drivendata-public-assets.s3.amazonaws.com/train_tier_2.tgz'
TEST_DATA = 'https://drivendata-public-assets.s3.amazonaws.com/test.tgz'


print('\nSelect the data you want to download - ')
print('-----------------------------------------')
print('|Id\t|\tDataset\t\t\t|')
print('-----------------------------------------')
print('|1\t|\tTrain Tier 1 dataset\t|')
print('|2\t|\tTrain Tier 2 dataset\t|')
print('|3\t|\tTest dataset\t\t|')
print('-----------------------------------------')
val = input('Enter the dataset id:')

url = ''

if val == '1':
    url = TRAIN_TIER_1
elif val == '2':
    url = TRAIN_TIER_2 
elif val == '3':
    url = TEST_DATA
else :
    print('\nInvalid dataset id entered')
    exit()


filename = wget.download(url)
