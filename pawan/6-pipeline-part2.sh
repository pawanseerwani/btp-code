if [ "$#" -ne 3 ];
	then 
    echo -e "Error: Incorrect usage. Use $0 <brand-name> <product-name> <limit>"
	exit
fi 

echo -e "The following parameters were given
brand:$1 
product:$2 
limit:$3

Starting data extraction..." && 
python 0-autoextraction.py "$2" "$3" && 
echo -e "Finished extraction...\n" && 

echo -e "Starting Preprocessing..." && 
python 2-preprocess.py "$2" && 
echo -e "Finsished Preprocessing..\n" &&

echo -e "Starting Lemmatization..." && 
python 3-lemmatize.py  "$2" && 
echo -e "Finished Lemmatization...\n"

echo -e "Starting Product analyser...(This could take a while)" && 
python 4-product_analyser.py "$2" "$1" "$2"  && 
echo -e "Finsished product analysis...\n"

echo -e "Starting graph generation..." &&
python 5-graph_generator.py &&
echo -e "Finished graph generation...\n" &&

echo -e "Thank you for using our application! :) \n"
