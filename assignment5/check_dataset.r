
checkdataset_markpeng <- function() {
  # Read dataset
  filePath <- "E:/VM/Share/datasci_course_materials/assignment5/seaflow_21min.csv"
  dataset <- read.csv(filePath, header=TRUE)
  # print(paste('nrows:',nrow(dataset)))  
  # print(paste('ncol:',ncol(dataset)))
  
  ## Q13
  #df <- melt(dataset, id='time', variable_name='features')
  
  # plot on same grid, each series colored differently -- 
  # good if the series have same scale
  # ggplot(df, aes(time,value)) + geom_line(aes(colour=features))
  
  # or plot on different plots
  # ggplot(df, aes(time,value)) + geom_line() + facet_grid(features ~ .)

  # plot.ts(dataset[,c("fsc_small", "fsc_perp", "fsc_big", "pe", "chl_small", "chl_big")],
  #                 main="Distribution of features")

  ## Q14
  # Save ggplot() as object
  graph <- ggplot(data=dataset, aes(x=time,y=chl_big))
  # Add graph to geom_line()
  graph + geom_point()
  
}

# require(ggplot2)
# require(reshape)
# checkdataset_markpeng()
