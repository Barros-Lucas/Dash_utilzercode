Ce dossier ne doit contenir uniquement le script python, le script bash ainsi que les deux images à traité pour éviter tous conflits possibles

Ne modifier ni le script python ni le script bash.

Lancez à l'aide de cette ligne de commande le docker:
	docker run -ti -p 5000:8080 -v /yourPath/:/home/Dash sousouc/dashut
	(Pour plus d'information rendez-vous sur le docker hub de sousouc pour en savoir plus sur la commande entré)

Une fois sur le docker :
	*vérifiez d'être bien dans le repertoire /home/Dash*
	python dashut_l.py

Sur la page web Dash un message s'affichera quand le traitement sera affectué.
Allez dans le repertoire results pour retrouver vos images recalées.
