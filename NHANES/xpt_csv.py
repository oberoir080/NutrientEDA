import pyreadstat

# Load XPT file
xpt_data, meta = pyreadstat.read_xport("secondDay.xpt")

# Write to CSV
xpt_data.to_csv("secondDay.csv", index=False)
