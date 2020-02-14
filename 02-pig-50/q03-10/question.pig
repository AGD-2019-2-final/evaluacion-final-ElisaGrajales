-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
fs -rm output/*
fs -rmdir  output
fs -rm -f -r data.tsv
fs -put data.tsv

Tabla = LOAD 'data.tsv' USING PigStorage()
    AS (Letra:CHARARRAY,
        Fecha:CHARARRAY,
        Num:INT);
Ordenado = ORDER Tabla BY Num;
r = FOREACH Ordenado GENERATE Num;
z = LIMIT r 5;
DUMP z;

STORE z INTO 'output';

fs -copyToLocal output 