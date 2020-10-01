library("plyr")
library("ggplot2")
attach(luganda)

ggplot (luganda, aes (x = f2, y = f1, label = vowel, col = vowel))  + geom_text(size = 4) + ylim (900, 200) + xlim (3000,800) + xlab ("F2 (Hz)") + ylab ("F1 (Hz)") + ggtitle ("F1 and F2 by vowel")+theme_bw()+ scale_color_manual (name = "Vowel", values = c("red", "blue", "green4", "black", "purple"), guide =FALSE)

vowel1 = ddply(luganda, c ("vowel"), summarize, N = length ("vowel"), meanf1 =    
                 mean (f1), sdf1 = sd(f1), meanf2 = mean (f2), sdf2 = sd(f2))

ggplot (vowel1, aes (x = meanf2, y = meanf1, label = vowel))  + geom_text(size = 6) + ylim (900, 200) + xlim (3000,800) + xlab ("F2 (Hz)") + ylab ("F1 (Hz)") + ggtitle ("Mean F1 and F2 by vowel")+theme_bw()
