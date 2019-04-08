# set general property
set grid
#set title "Number of Blocks per Month" font "Times-Roman"

set tics font "Times-Roman"
# set x-axis property
# Do not set x data of time type, see http://psy.swansea.ac.uk/staff/carter/gnuplot/gnuplot_time_histograms.htm
set xlabel "Time (month)" font "Times-Roman"
# set x data type back to normal. xdata type may still be time if we load this script twice because the second
# graph set xdata to time.
set xdata
# set xdata time
# # the timefmt here is used to set xrange
# set timefmt "%Y-%m"
# set xrange ["2016-12":"2018-05"]
# set format x "%Y-%m"
# set xtics "2016-12", 2592000, "2018-05"
set xtics rotate


# set y-axis property
set ylabel "Number of Blocks" font "Times-Roman"
set yrange [0:220000]
set ytics 20000 
set grid ytics

# set graph style
set style data histograms
set style histogram rowstacked
set boxwidth 0.5 relative
set style fill solid 1.0 border -1

# set data file property
set datafile separator ","

# output set
## If jpeg is wanted, use ---- set terminal jpg color enhanced "Helvetica" 20  set output "output.jpg"
# set terminal png medium
# set output "Number_of_blocks.png"

# In the csv file, 1st column is time, 2nd column is pool-mined, 4th column is non-pool-mined
# set term x11 0 # used when different window to display picture is wanted.
plot "../data/ether_monthly_data.csv" using 2:xticlabels(1) title 'pool-mined', \
"../data/ether_monthly_data.csv" using 4 title 'non-pool-mined'


