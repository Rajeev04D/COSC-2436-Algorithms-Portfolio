## Lab Report 12

**Name:** [Rajeev Oad]  
**Date:** [5/1/2026]  
**Algorithm Analysis:** K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction

---

## Algorithm Understanding

**What type of problem is this algorithm solving?**  
This algorithm solves a supervised learning / regression / prediction problem.

**How does KNN regression differ from KNN classification?**  
KNN regression predicts a continuous outcome by averaging the target values of the k-nearest neighbors, while KNN classification predicts a categorical outcome by majority voting among the neighbors.

**What does the "K" in KNN represent, and why did we choose k=4 for this problem?**  
The "K" represents the number of nearest neighbors considered. We chose k=4 to balance between too much variance (k=1) and too much bias (k being too large).

**In your own words, explain how the model produces a prediction for a new day.**  
The model finds the k closest historical days based on weather, weekend/holiday, and game status and averages their loaf counts to predict for a new day.

---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?**  
Separating features and target allows us to clearly define input variables and the output we want to predict, a standard practice in machine learning.

**Why must the input to `model.predict()` be a 2D array?**  
The model expects input in the same format used during training, which is a 2D array, to ensure consistency even if predicting a single sample.

**What does `.fit(X, y)` actually do for a KNN model?**  
KNN is a "lazy learner," so fitting simply stores the data for comparison rather than forming a complex internal model.

**Why do we use `.values` when extracting columns from the DataFrame?**  
Using `.values` converts DataFrame columns into numpy arrays, making them compatible with machine learning libraries like scikit-learn.

---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.**  
A limitation is sensitivity to the scale of features. It may predict poorly if features vary widely in range without scaling.

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?**  
More data could improve predictions by capturing more patterns, reducing overfitting to noise in a smaller dataset.

**What other features could the bakery collect to improve predictions?**  
Additional features like temperature, season, local events, and day of the week could enhance predictions.

**KNN is sometimes called a "lazy learning" algorithm. What is the prediction time tradeoff?**  
Prediction can be slow as it requires comparing against every training point, especially in large datasets.

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess?**  
ML predictions offer consistency, data-driven accuracy, scalability, and help reduce waste.

**If the bakery wanted to minimize waste, how might you change the approach?**  
Using a different loss function or adjusting predictions to slightly under-predict based on cost analysis of waste vs. lost sales could be effective.