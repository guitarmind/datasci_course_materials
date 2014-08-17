
assignment5_markpeng <- function() {
  # Read dataset
  filePath <- "E:/VM/Share/datasci_course_materials/assignment5/seaflow_21min.csv"
  data <- read.csv(filePath, header=TRUE)
  print(paste('nrows:',nrow(data)))  
  print(paste('ncol:',ncol(data)))
  
  filteredData <- subset(data, !(file_id==208))

  # Get all distinct class labels
  popClasses <- unique(as.factor(filteredData$pop))
  # print(popClasses)
  # summary(data)
  
  # Create training and testing dataset
  trainIndex <- createDataPartition(filteredData$pop, p=0.5, list=FALSE, times=1)
  # head(trainIndex)
  trainingData <- filteredData[trainIndex,]
  testingData <- filteredData[-trainIndex,]
  print(paste('training nrows:',nrow(trainingData)))  
  print(paste('training ncol:',ncol(trainingData)))
  print(paste('testingData nrows:',nrow(testingData)))  
  print(paste('testingData ncol:',ncol(testingData)))
  
  trainingTimeMean <- mean(trainingData$time, na.rm=TRUE)
  print(paste('Mean of time in training data:', trainingTimeMean))
  
  # Save ggplot() as object
  # graph <- ggplot(data=trainingData, aes(x=pe,y=chl_small,colour=pop))
  # Add graph to geom_line()
  # graph + geom_line()
  # print(head(trainingData, 50))
  # summary(trainingData)
  
  ##############################################################
  ## Train a decision tree
  
  # Create a formula from a string
  fol <- as.formula("pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small")
  # fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
  model <- rpart(fol, method="class", data=trainingData)
  # print(model)
  
  
  # Evaluate the decision tree on the test data
  predictions <- predict(model, newdata=testingData, type="class")
  # print(typeof(predictions))
  # print(head(predictions, 5))
  output <- (predictions == testingData$pop)
  # print(head(output, 50))
  # correct_num <- length(output[output==TRUE])
  correct_num <- sum(output, na.rm=TRUE)
  print(paste('correct_num:',correct_num))
  
  # Compute testing accuracy
  test_accuracy <- correct_num / nrow(testingData)
  print(paste('decision tree test_accuracy:',test_accuracy))
  
  print(table(pred=predictions, true=testingData$pop))
  
  ##############################################################
  ## Build and evaluate a random forest
  model <- randomForest(fol, method="class", data=trainingData)
  predictions <- predict(model, newdata=testingData, type="class")
  
  output <- (predictions == testingData$pop)
  correct_num <- sum(output, na.rm=TRUE)
  print(paste('correct_num:',correct_num))
  
  # Compute testing accuracy
  test_accuracy <- correct_num / nrow(testingData)
  print(paste('random forest test_accuracy:', test_accuracy))
  
  print(table(pred=predictions, true=testingData$pop))
  
  # Compute model importance for gini impurity measure
  # importance(model)

  ##############################################################
  # Train a support vector machine model
  model <- svm(fol, method="class", data=trainingData)
  predictions <- predict(model, newdata=testingData, type="class")
  
  output <- (predictions == testingData$pop)
  correct_num <- sum(output, na.rm=TRUE)
  print(paste('correct_num:',correct_num))
  
  # Compute testing accuracy
  test_accuracy <- correct_num / nrow(testingData)
  print(paste('svm test_accuracy:', test_accuracy))
  
  print(table(pred=predictions, true=testingData$pop))
}

# main()
library("caret")
library("rpart")
library("randomForest")
library("e1071")
set.seed(1)
assignment5_markpeng()

