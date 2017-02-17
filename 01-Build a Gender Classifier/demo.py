from sklearn import tree

clf = tree.DecisionTreeClassifier()

# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data

clf = clf.fit(X, Y)

dad_prediction = clf.predict([[171, 74, 42]])
mom_prediction = clf.predict([[165, 63, 39]])
josh_prediction = clf.predict([[152, 41, 40]])
lucas_prediction = clf.predict([[170, 52, 42]])
julian_prediction = clf.predict([[178, 59, 44]])

# CHALLENGE compare their reusults and print the best one!

print dad_prediction, mom_prediction, josh_prediction, lucas_prediction, julian_prediction
