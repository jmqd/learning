library(ggplot2)

data = read.csv("active_previous_order.csv", header = TRUE, stringsAsFactors = FALSE)
ggplot(data, aes(x=days)) + 
  stat_bin(binwidth=14) +
  xlim(c(-7, 220)) + 
  ylim(c(0,7800)) +
  stat_bin(binwidth=14, geom="text", aes(label=..count..), vjust=-1.0)
