library(ggplot2)
library(forecast)

data = read.csv("daily_sales.csv", header = TRUE, stringsAsFactors = FALSE)
data_ts <- msts(data, seasonal.periods = c(7, 365.25))
fit <- tbats(data_ts, use.trend = TRUE, use.parallel = TRUE, seasonal.periods = c(7, 365.25))
fc <- forecast(fit)
plot(fc)
