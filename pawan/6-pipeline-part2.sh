DEBUG="0"
declare -A product
declare -a count=('first' 'second' 'third');
<<COMMENT
if [ "$#" -ne 3 ];
	then 
    echo -e "Error: Incorrect usage. Use $0 <brand-name> <product-name> <limit>"
	exit
fi 

COMMENT
if [ $DEBUG = "0" ]
    then
        for i in {0..1}
        do
            read -p "Enter a brand name: " brand[$i]
            for j in {0..2}
            do
                read -p "Enter the ${count[$j]} product(-1 to skip): " product[$i,$j]

                if [ ${product[$i,$j]} == "-1" ]
                    then
                    break
                fi
            done
        done
        echo -e ""
        read -p "Enter max no of tweets per product: " limit
else
        brand[0]="apple"
        product[0,0]="iphone"
        brand[1]="samsung"
        product[1,0]="noteII"
        limit=10
fi

<<COMMENT2
echo ${brand[0]}
echo ${product[0,0]}
echo ${brand[1]}
echo ${product[1,0]}
COMMENT2
for i in {0..1}
do
    for j in {0..2}
    do
        curr_brand=${brand[$i]}
        curr_product=${product[$i,$j]}
        if [ $curr_product == "-1" ]
            then
                break
        fi
        mixed="$curr_brand $curr_product"

        echo -e "The following parameters are being considered
        brand: $curr_brand 
        product: $curr_product
        "
    
        echo -e "Starting data extraction..." && 
        python 0-autoextraction.py "$mixed" "$limit" && 
        echo -e "Finished extraction...\n" && 

        echo -e "Starting Preprocessing..." && 
        python 2-preprocess.py "$mixed" && 
        echo -e "Finsished Preprocessing..\n" &&

        echo -e "Starting Lemmatization..." && 
        python 3-lemmatize.py  "$mixed" && 
        echo -e "Finished Lemmatization...\n"

        echo -e "Starting Sentiment identification and classification.. (This could take a while)" &&
        python 4-product_analyser.py "$mixed" "$curr_brand" "$curr_product"  && 
        echo -e "Finsished product analysis...\n"

        echo -e "Starting graph generation..." &&
        python 5-graph_generator.py  "$mixed" &&
        echo -e "Finished graph generation...\n" &&
       
        sleep 5
        clear
    done
done

python 7-brand_graph_generator.py  "${brand[0]}" "${brand[1]}"
echo -e "\nThank you for using our application! :) \n"
