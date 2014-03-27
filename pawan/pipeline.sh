if [ "$#" -ne 3 ];
	then 
    echo "Error: Incorrect usage. Use $0 <raw-html-file-name> <brand-name> <product-name>"
	exit
fi 

python 1-extract.py $1 && python 2-preprocess.py $1 && python 3-lemmatize.py  $1 && python 4-product_analyser.py $1 $2 $3
