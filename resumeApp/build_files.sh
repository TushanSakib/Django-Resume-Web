echo "BUILD START"
python3.11.4 -m pip install -r requirments.txt
python3.11.4 manage.py collectstatic --noinput --clear
echo "BUILD END"