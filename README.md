# NTL initiative: Facts and insights  

NTL is an initiative from the Egyptian ministry of telecommunications  
to help graduates take online courses for free as a grant,  
provided that the student finish his/her course before a deadline.  

I scraped the data of the graduates using this script [ntl_extract.py](ntl_extract.py)  
and made a Tableau story about it to highlight important insights out.  

I derived two new dimensions from the dataset:  

* Course-site: which is the online site on which the track is available  
* Urban-region: which is the region of the country to which the graduate belongs

the original site from which I scraped the data is: [ntl wall of fame](http://techleaders.eg/wall-of-fame/)


## Getting started

Simply click this link [NTL: Facts and insights](https://public.tableau.com/profile/ahmed.eweed#!/vizhome/Book1_15741837906850/NTLQuickAnalysisandInsights)  
and explore the story page by page.  
any questions are welcomed at my facebook account mentioned at the end of the story

## Prerequisites

Nothing special to view the story, Just click the link [NTL: Facts and insights](https://public.tableau.com/profile/ahmed.eweed#!/vizhome/Book1_15741837906850/NTLQuickAnalysisandInsights)  

If you want to reproduce the results (reaquire the dataset)  
run the script on any place on your machine  
and it will produce the dataset for you named `ntl_data.csv`  

you should have at least python 3.4 or higher installed  
and for sure you must have all the libraries imported installed! 

## Authors

* **Ahmed Eweed** - *Initial work* - [AhmedEweed](https://github.com/AhmedEweed)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements  

The data used in this Tableau Story was scraped from ntl page [ntl wall of fame](http://techleaders.eg/wall-of-fame/)  

All rights reserved.