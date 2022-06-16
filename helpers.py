from sklearn.utils import resample
# Binary classification resampling function.
def grow_class(X_train,y_train, smaller_class, seed):
    small_class = X_train[y_train == smaller_class]
    not_small_class = X_train[y_train != smaller_class]

    print("Smaller class samples: {}".format(small_class.shape[0]))

    # resample potable data points
    resampled_potable = resample(potable, n_samples=non_potable.shape[0] + 100, random_state=seed)
    print("Resampled potable samples: {}".format(resampled_potable.shape[0]))

    # Combine and shuffle the data.
    data = shuffle(pd.concat([non_potable, resampled_potable]), random_state=seed)
    print('New distribution of data:\n')
    data['Potability'].value_counts()


