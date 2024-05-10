from garmin_fit_sdk import Decoder, Stream
import matplotlib.pyplot as plt
import pandas as pd


def df_from_fit(file):
    stream = Stream.from_file(file)
    decoder = Decoder(stream)
    messages, errors = decoder.read()

    print(f"ERRORS: {errors}")
    print(messages.keys())

    df = pd.DataFrame(messages["record_mesgs"])
    print(df)

    plt.plot(df["distance"], df["heart_rate"], "b", label=file)
    plt.show()


def compare_fits(files):
    dfs = []

    for file in files:
        stream = Stream.from_file(file)
        decoder = Decoder(stream)
        messages, errors = decoder.read()

        df = pd.DataFrame(messages["record_mesgs"])
        dfs.append(df)
        print(df)

    metric = input(f"Metric to analyze {list(df.columns)}: ")

    plt.plot(dfs[0]["distance"], dfs[0][metric], "g", label=files[0])
    plt.plot(dfs[1]["distance"], dfs[1][metric], "c", label=files[1])
    plt.legend(loc="lower center")
    plt.title(metric)
    plt.show()


fit_file0 = input(
    "Name of first .fit file to analyze (must be in same directory as script): "
)
fit_file1 = input(
    "Name of second .fit file to analyze (must be in same directory as script): "
)
fit_files = [fit_file0, fit_file1]

compare_fits(fit_files)
