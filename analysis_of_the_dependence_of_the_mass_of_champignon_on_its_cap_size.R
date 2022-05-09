# Cap diameter and mass of champignon (centimeters/grams)
# Диаметр шляпки и масса шампиньона (сантиметры/граммы)
cap_diameter_big <- c(5.0, 5.7, 4.7, 5.2, 4.8, 4.9, 4.5, 5.2, 5.0, 4.8, 4.8, 5.0, 5.4, 5.2)
mass_big <- c(26.6, 29.6, 26.0, 24.9, 26.9, 24.4, 27.0, 30.4, 27.8, 27.1, 27.0, 28.1, 31.1, 28.7)
cap_diameter_small <- c(3.2, 2.5, 3.4, 3.7, 3.3, 3.5, 3.1, 2.8, 3.4, 3.4, 3.4, 3.0, 3.4, 3.7, 3.5, 3.6, 3.4, 3.1, 3.7, 3.4, 3.4, 3.4, 3.6)
mass_small <- c(11.2, 13.4, 12.2, 12.5, 11.3, 12.2, 8.9, 6.3, 10.7, 9.1, 11.7, 9.2, 10.6, 11.9, 12.0, 13.8, 10.7, 8.5, 14.2, 10.4, 10.7, 10.2, 13.6)

# General sampling options
# Общие параметры выборки
summary(cap_diameter_big)
summary(mass_big)
summary(cap_diameter_small)
summary(mass_small)

# Building a graph
# Построение графика
plot(cap_diameter_big, mass_big)
plot(cap_diameter_small, mass_small)

# Generalization of data and construction of a generalized scatterplot with the construction of a linear regression
# Обобщение данных и построение обобщенной диаграммы рассеяния с построением линейной регрессии
total_cap_diameter <- c(5.0, 5.7, 4.7, 5.2, 4.8, 4.9, 4.5, 5.2, 5.0, 4.8, 4.8, 5.0, 5.4, 5.2, 3.2, 2.5, 3.4, 3.7, 3.3, 3.5, 3.1, 2.8, 3.4, 3.4, 3.4, 3.0, 3.4, 3.7, 3.5, 3.6, 3.4, 3.1, 3.7, 3.4, 3.4, 3.4, 3.6)
total_mass <- c(26.6, 29.6, 26.0, 24.9, 26.9, 24.4, 27.0, 30.4, 27.8, 27.1, 27.0, 28.1, 31.1, 28.7, 11.2, 13.4, 12.2, 12.5, 11.3, 12.2, 8.9, 6.3, 10.7, 9.1, 11.7, 9.2, 10.6, 11.9, 12.0, 13.8, 10.7, 8.5, 14.2, 10.4, 10.7, 10.2, 13.6)
data <- data.frame(total_cap_diameter, total_mass)
plot(data$total_cap_diameter, data$total_mass, xlab = 'Размер шляпки, см', ylab = 'Масса шампиньона, гр')

# Influence of the cap diameter on the mass of champignon (regression construction)
# Влияние диаметра шляпки на массу шампиньона (построение регрессии)
# y <- -18.881+9.106*x
abline(lm(total_mass ~ total_cap_diameter, data=data), col='red')
lm_mass_diameter <- lm(total_mass ~ total_cap_diameter)
lm_mass_diameter
