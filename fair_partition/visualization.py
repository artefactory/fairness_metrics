import matplotlib.pyplot as plt


def plot_partition(partition, phi_by_group, sensitive_var_name="ITA"):
    for i in range(len(partition)):
        plt.axvline(x=partition[i], color="black", linestyle="dashed")

    for i in range(len(partition) - 1):
        plt.hlines(y=phi_by_group[i], xmin=partition[i], xmax=partition[i + 1], color="red")

    plt.xlabel(f"${sensitive_var_name}$")
    plt.ylabel(rf"$\Phi({sensitive_var_name}^{{\mathcal{{P}}}})$")
    plt.show()


def plot_partition_with_ci(partition, partition_ci, sensitive_var_name="ITA"):
    for i in range(len(partition)):
        plt.axvline(x=partition[i], color="black", linestyle="dashed")

    for i in range(len(partition) - 1):
        plt.hlines(y=partition_ci[i, 0], xmin=partition[i], xmax=partition[i + 1], color="red")
        plt.fill_between(
            x=[partition[i], partition[i + 1]],
            y1=partition_ci[i, 2],
            y2=partition_ci[i, 1],
            color="orange",
            interpolate=True,
            alpha=0.5,
        )

    plt.xlabel(f"${sensitive_var_name}$")
    plt.ylabel(rf"$\Phi({sensitive_var_name}^{{\mathcal{{P}}}})$")
    plt.show()


def plot_conditional_proba(s_bins, y_s_proba, sensitive_var_name="ITA"):
    plt.plot(s_bins[:-1], y_s_proba)
    plt.xlabel(f"${sensitive_var_name}$")
    plt.ylabel(rf"$P(Y = 1 | {sensitive_var_name})$")
    plt.show()
