###########################################################
########### MIT license 2022 Vladimir Shalyapin ###########
###########            R version 4.1.1          ###########
###########################################################
 
epochs <- c("10", "100", "250", "500", "1000")
learning_rate <- c("0.1", "0.3", "0.5", "1.0")
palet=colorRampPalette(c("black","white"))
colors=palet(4)
 
# Create the matrix of the values.
Values <- matrix(c(0.0, 0.8, 0.6, 0.8, 0.7, 0.4, 0.8, 0.8, 0.7, 0.7, 0.5, 0.8, 0.6, 0.7, 0.7, 0.4, 0.7, 0.6, 0.4, 0.5),
                 nrow = 4, ncol = 5, byrow = TRUE)
 
# Create the bar chart
barplot(Values, main = "Оценка работы нейронной сети при изменении эпох и скорости обучения", names.arg = epochs,
                          xlab = "epochs", ylab = "performance",
                          beside = TRUE)
 
# Add the legend to the chart
legend("topleft", learning_rate, cex = 0.7, fill = colors)
