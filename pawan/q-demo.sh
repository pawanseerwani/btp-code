if [ "$#" -ne 3 ];
	then 
    echo "Error: Incorrect usage. Use $0 <csv-file-name> <brand-name> <product-name>"
	exit
fi 

echo "Starting Preprocessing...\n" && python 2-preprocess.py $1 && echo "Finsished Preprocessing..\n\n Starting Lemmatization...\n" && python 3-lemmatize.py  $1 && echo "Finished Lemmatization...\n\n Starting Analysis...\n(This could take a while)\n" && python 4-product_analyser.py $1 $2 $3 && echo "Finsished analysis...\n\n Thank you for using our application! :) \n\n"
