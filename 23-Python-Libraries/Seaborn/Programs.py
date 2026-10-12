import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")
sns.lineplot(x="timepoint", y="signal", hue="region", data=fmri)
plt.show()
