if [ "$#" -ne 3 ];
	then 
    echo "Error: Incorrect usage. Use $0 <raw-html-file-name> <brand-name> <product-name>"
	exit
fi 

echo "Starting extraction of tweets from html to csv format...\n" && python 1-extract.py $1 && echo "Finished extraction...\nStarting Preprocessing...\n" && python 2-preprocess.py $1 && echo "Finsished Preprocessing..\n\n Starting Lemmatization...\n" && python 3-lemmatize.py  $1 && echo "Finished Lemmatization...\n\n Starting Analysis...\n(This could take a while)\n" && python 4-product_analyser.py $1 $2 $3 && echo "Finsished analysis...\n\n Thank you for using our application! :) \n\n"
