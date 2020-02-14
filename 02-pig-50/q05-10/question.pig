-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

fs -put data.tsv
Tabla = LOAD 'data.tsv' USING PigStorage()
    AS (Letra:CHARARRAY,
        Minuscula:CHARARRAY,
        Combinado:CHARARRAY);
Col2 = FOREACH Tabla GENERATE $1;
letters = FOREACH Col2 GENERATE FLATTEN (TOKENIZE(Minuscula)) AS Letras;
grouped = GROUP letters BY Letras;
lettercount = FOREACH grouped GENERATE group, COUNT(letters);
DUMP lettercount;
store lettercount into 'output';
fs -copyToLocal output