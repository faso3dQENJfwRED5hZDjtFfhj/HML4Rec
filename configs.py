configs = {
    # item side information
    'num_rate': 6,
    'num_genre': 25,
    'num_director': 2186,
    'num_actor': 8030,
    'embedding_dim': 32,
    # user side information
    'num_gender': 2,
    'num_age': 7,
    'num_occupation': 21,
    'num_zipcode': 3402,
    #hyper-parameters
    'safety_margin_size' : 0.2,
    'iterations' : 1000,
    'durations' : 14,
    'global_lr' : 1e-3,
    'local_lr' : 5e-5,
    'market_lr' : 5e-4,
    'ways_t' : 16, # periods number per mini-batch
    'ways_s' : 20, # users number per period
    'min_pchs' : 6,
    'len_query_i' : 3,
}