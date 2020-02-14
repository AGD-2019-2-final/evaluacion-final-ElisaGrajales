-- Pregunta
-- ===========================================================================
-- 
-- Ordene el archivo `data.tsv`  por letra y valor (3ra columna).
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
--  >>> Escriba el codigo del mapper a partir de este punto <<<
-- 
fs -rm output/*
fs -rmdir  output
fs -rm -f -r data.tsv
fs -put data.tsv

Tabla = LOAD 'data.tsv' USING PigStorage()
    AS (Letra:CHARARRAY,
        Fecha:CHARARRAY,
        Num:INT);
Ordenado = ORDER Tabla BY Letra, Num;
DUMP Ordenado;

STORE Ordenado INTO 'output';

fs -copyToLocal output