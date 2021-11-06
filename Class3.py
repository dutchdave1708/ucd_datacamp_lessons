# class 3
# for <any name> in enumerate(list) --> the enumerate means you also access the index data
# installed Git on macbook via Homebrew
# install Homebrew dave$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# install Git : Daves-MacBook-Air:~ dave$ $ brew install git
# create GitHub account
# update PyCharm to link to GitHub account
# link PyCharm project to GitHub repo
# commit&push the existing files to GitHub

#import numpy package
import numpy as np
np.random.seed(123)

#print(np.random.random())


# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

