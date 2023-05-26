# Breast Cancer Prediction
<h2> Description </h2>
<p>The project is to Predict whether the patient will die because of breast cancer or not 
used data which mentions the symptoms of the patient.
  we performed data cleaning and preprocessing & trained several models with it.</p>
<p>Performed Data Exploration to know our data and to find outliers,Null Values,Inconsistent or wrong data</p>
<p>Performed multiple visualizations to have more understanding of the data and the relation of attributes to each other
  and how every attribute affect another</p>
<p>Performed Data Cleaning by outliers,Null Values,Inconsistent or wrong data, We discretized the age</p>
<p>The data was imbalanced so we chose to oversample the minority of the data</p>
<p>Made Feature Selection dependent on the correlation between attributes and each other and between the
  target & then we extracted the features we needed</p>
<p>Finally used multiple models to predict our targets
  <h2>Models</h2>
  <ul>
    <li>Logistic Regression</li>
    <li>Random Forest</li>
    <li>KNN</li>
    <li>SVM</li>
    <li>Naive Bayes</li>
  </ul>
</p>
<p>We found the model with the best accuracy which was Random Forest which was 95% , So we Deployed it using Flask
Made a website to take the symptoms of the patient and predict whether they will live or have a high risk to die.</p>
