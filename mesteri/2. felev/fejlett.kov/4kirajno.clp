 
(deffacts init
	(rows 9)     ; (rows 1 2 3 4 5 6)
	(table)
)
 
(defrule append-rows
	?f <- (rows ?a & ~1 $?tail) ; (test (> ?a 1))
	=>
	(assert (rows (- ?a 1) ?a ?tail))
	(retract ?f)
)
 
(defrule insert
	(table $?list)
	(rows $? ?r $?)
	(rows $? ?size)
	(test (< (length$ $?list) ?size))
	=>
	(assert (table ?r $?list))
)
 
(defrule delete-row (declare (salience 1))
	?f <- (table ?a $? ?a $?)
	=>
	(retract ?f)
)
 
(defrule delete-diag (declare (salience 1))
	?f <- (table ?a $?list ?b $?)
	(test (= (+ (length$ $?list) 1) (abs (- ?a ?b))))
	=>
	(retract ?f)
)
 
(defrule delete-partial (declare (salience -1))
	?f <- (table $?list)
	(rows $? ?size)
	(test (< (length$ $?list) ?size))
	=> 
	(retract ?f)
)
 
 
(reset)
(run)
(facts)
 
