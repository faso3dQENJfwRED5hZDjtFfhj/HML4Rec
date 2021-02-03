# HML4Rec
The source code of paper "HML4Rec: Hierarchical Meta-Learning for Cold-StartRecommendation in Flash-Sale E-commerce" for reproduction.

## Usage
Experiment.ipynb shows an example about our experiment on MovieLens 1M. 

### Requirements
- python 3.7+
- pytorch 1.1+
- pandas 1.1+
- numpy 1.19+
- scipy 1.5+

### Preparing data
```python
train_order, valid_order, test_order, movie_dict, user_dict, Tr_rated_dict, Rated_dict, condidate_item = prepare_dataset()
```

### Initializing a model
```python
RecSys = HML4Rec(configs, train_order, valid_order, test_order, movie_dict, user_dict, Tr_rated_dict, Rated_dict, condidate_item)
```

### Training
```python
RecSys.train()
```

### generating results and evaluating
```python
RecSys.Recommending()
Show_result()
```
