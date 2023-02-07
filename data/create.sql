CREATE TABLE "inversiones" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
    "time"	TEXT NOT NULL,
	"Moneda_from"	TEXT NOT NULL,
	"Quantity_from"	REAL NOT NULL,
    "Moneda_to"	TEXT NOT NULL,
	"Quantity_to"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)