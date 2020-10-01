library("ggplot2")

attach (results)
mid = subset(results, time=="50")
ggplot (mid, aes (x = f2, y = f1, label = interval))  + geom_text () + ylim (1000, 300) + xlim (3000,700) + xlab ("F2 (Hz)") + ylab ("F1 (Hz)")+theme_bw() + ggtitle ("Formant frequencies at vowel midpoint")

time1 = subset (results, time !="50")
ggplot (time1, aes (x = f2, y = f1, group = interval, label = interval))  + geom_path (arrow = arrow (ends = "last", length = unit (0.1, "inches"))) + geom_text() + ylim (1000, 300) + xlim (3000,700) + xlab ("F2 (Hz)") + ylab ("F1 (Hz)")+theme_bw() +ggtitle ("Formant trajectories from 20% to 80% of vowel duration")
