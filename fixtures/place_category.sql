--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.1
-- Dumped by pg_dump version 9.5.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

--
-- Data for Name: place_category; Type: TABLE DATA; Schema: public; Owner: jgarciadiaz
--

COPY place_category (id, name) FROM stdin;
1	Autos
3	Comida
4	Tienda
5	Belleza
6	Salud
7	Educación
2	Bar
8	Ejercicio
9	ropa
10	Servicios
11	Entretenimiento
\.


--
-- Name: place_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jgarciadiaz
--

SELECT pg_catalog.setval('place_category_id_seq', 11, true);


--
-- PostgreSQL database dump complete
--

