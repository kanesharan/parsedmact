import pandas, os, random

def random_sample(dataframein):
    beginning_splice = random.randint(1, len(dataframein)-100)
    ending_splice = random.randint(beginning_splice, beginning_splice+100)
    return dataframein.iloc[beginning_splice:ending_splice,:]

def parse_to_mact(filename):
    df = pandas.read_csv(filename, index_col=['count'])
    df = random_sample(df)
    df.reset_index(inplace=True)
    df = df[['event type','timestamp','x','y']]
    mactout = ''
    for index,row in df.iterrows():
        currow = map(str,[index, *row.values])
        mactout += ','.join(currow)+';'
    print(mactout)

parse_to_mact('user7_session_0557467514.csv')