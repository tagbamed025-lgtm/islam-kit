D=$1; cd /home/claude/musab_reels
python3 ev.py $D && cd $D && python3 ../pad.py && python3 ../sfx.py && bash /home/claude/musab/mix2.sh
