E=/home/claude/islam-kit/moteur/apparition-commun
for ID in COMP-03-umm-ammara COMP-04-julaybib COMP-05-abu-ayyub COMP-06-zayd; do
  bash $E/final.sh /home/claude/travail/comp/$ID 2 > /home/claude/travail/comp/$ID/final.log 2>&1
done
echo ALLDONE > /home/claude/travail/comp/done.txt
