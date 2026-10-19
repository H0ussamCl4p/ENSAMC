# Jeu de données gapminder : résumé, dplyr, test de Student, ggplot2
# À installer une seule fois :
# install.packages(c("gapminder", "dplyr", "ggplot2"))

library(gapminder)
library(dplyr)
library(ggplot2)

data("gapminder")
summary(gapminder)
mean(gapminder$gdpPercap)

# Espérance de vie moyenne : Afrique du Sud vs Irlande
gapminder %>%
  select(country, lifeExp) %>%
  filter(country == "South Africa" | country == "Ireland") %>%
  group_by(country) %>%
  summarise(Avg_life = mean(lifeExp))

# Test t : la différence d'espérance de vie entre les deux pays est-elle significative ?
df1 <- gapminder %>%
  select(country, lifeExp) %>%
  filter(country == "South Africa" | country == "Ireland")

t.test(data = df1, lifeExp ~ country)

# PIB par habitant (log) vs espérance de vie, par continent
gapminder %>%
  filter(gdpPercap < 50000) %>%
  ggplot(aes(x = log(gdpPercap), y = lifeExp)) +
  geom_point(aes(col = year, size = pop), alpha = 0.3) +
  geom_smooth(method = lm) +
  facet_wrap(~continent)
