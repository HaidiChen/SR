sudo docker build -t flask/app .

cd ..
if [ -e "shared_folder" ]
then
    rm shared_folder -rf
fi
mkdir shared_folder
cd shared_folder

sudo docker run --rm --name fp -p 5000:5000 -v `pwd`:/sf flask/app
