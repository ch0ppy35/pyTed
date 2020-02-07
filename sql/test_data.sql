--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: killawatts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.killawatts (
    id integer NOT NULL,
    killawatts real,
    ts timestamp without time zone DEFAULT now()
);


ALTER TABLE public.killawatts OWNER TO postgres;

--
-- Name: killawatts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.killawatts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.killawatts_id_seq OWNER TO postgres;

--
-- Name: killawatts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.killawatts_id_seq OWNED BY public.killawatts.id;


--
-- Name: kwhtotals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kwhtotals (
    id integer NOT NULL,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.kwhtotals OWNER TO postgres;

--
-- Name: kwhtotals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kwhtotals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kwhtotals_id_seq OWNER TO postgres;

--
-- Name: kwhtotals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kwhtotals_id_seq OWNED BY public.kwhtotals.id;


--
-- Name: kwhtotalsday; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kwhtotalsday (
    id integer NOT NULL,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.kwhtotalsday OWNER TO postgres;

--
-- Name: kwhtotalsday_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kwhtotalsday_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kwhtotalsday_id_seq OWNER TO postgres;

--
-- Name: kwhtotalsday_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kwhtotalsday_id_seq OWNED BY public.kwhtotalsday.id;


--
-- Name: kwhtotalsmonth; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kwhtotalsmonth (
    id integer NOT NULL,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.kwhtotalsmonth OWNER TO postgres;

--
-- Name: kwhtotalsmonth_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kwhtotalsmonth_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kwhtotalsmonth_id_seq OWNER TO postgres;

--
-- Name: kwhtotalsmonth_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kwhtotalsmonth_id_seq OWNED BY public.kwhtotalsmonth.id;


--
-- Name: pyteddbver; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pyteddbver (
    id integer NOT NULL,
    dbver real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.pyteddbver OWNER TO postgres;

--
-- Name: pyteddbver_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pyteddbver_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pyteddbver_id_seq OWNER TO postgres;

--
-- Name: pyteddbver_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pyteddbver_id_seq OWNED BY public.pyteddbver.id;


--
-- Name: voltage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voltage (
    id serial NOT NULL,
    voltage real,
    ts timestamp without time zone DEFAULT now()
);


ALTER TABLE public.voltage OWNER TO postgres;

--
-- Name: voltage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voltage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voltage_id_seq OWNER TO postgres;

--
-- Name: voltage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voltage_id_seq OWNED BY public.voltage.id;


--
-- Name: killawatts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.killawatts ALTER COLUMN id SET DEFAULT nextval('public.killawatts_id_seq'::regclass);


--
-- Name: kwhtotals id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kwhtotals ALTER COLUMN id SET DEFAULT nextval('public.kwhtotals_id_seq'::regclass);


--
-- Name: kwhtotalsday id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kwhtotalsday ALTER COLUMN id SET DEFAULT nextval('public.kwhtotalsday_id_seq'::regclass);


--
-- Name: kwhtotalsmonth id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kwhtotalsmonth ALTER COLUMN id SET DEFAULT nextval('public.kwhtotalsmonth_id_seq'::regclass);


--
-- Name: pyteddbver id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pyteddbver ALTER COLUMN id SET DEFAULT nextval('public.pyteddbver_id_seq'::regclass);


--
-- Name: voltage id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voltage ALTER COLUMN id SET DEFAULT nextval('public.voltage_id_seq'::regclass);


--
-- Data for Name: killawatts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.killawatts (id, killawatts, ts) FROM stdin;
1	9.696	2020-02-05 19:27:16.607645
2	9.946	2020-02-05 19:27:31.4161
3	6.618	2020-02-05 19:30:08.639516
4	6.612	2020-02-05 19:30:31.246355
5	6.816	2020-02-05 19:41:29.948288
6	6.816	2020-02-05 19:41:31.170129
7	12.376	2020-02-05 19:44:42.44607
8	10.804	2020-02-05 19:45:05.232861
9	10.804	2020-02-05 19:45:31.201479
10	10.87	2020-02-05 19:46:01.216869
11	7.284	2020-02-05 19:46:31.125382
12	7.248	2020-02-05 19:47:01.584831
13	7.29	2020-02-05 19:47:31.873617
14	7.13	2020-02-05 19:48:01.692692
15	7.314	2020-02-05 19:48:32.424073
16	6.744	2020-02-05 19:49:04.660653
17	6.764	2020-02-05 19:49:31.382312
18	6.802	2020-02-05 19:50:01.507089
19	6.736	2020-02-05 19:50:31.411431
20	6.488	2020-02-05 19:59:06.584158
21	5.324	2020-02-05 20:07:34.574981
22	1.826	2020-02-05 20:09:29.849458
23	1.826	2020-02-05 20:09:31.145528
24	2.218	2020-02-05 20:15:46.266029
25	1.8	2020-02-05 20:23:36.374499
26	2.144	2020-02-05 20:23:54.190363
27	5.458	2020-02-05 20:31:31.527017
28	5.458	2020-02-05 20:31:31.694342
29	5.628	2020-02-05 20:31:47.52309
30	5.498	2020-02-05 20:31:57.987408
31	1.678	2020-02-05 20:43:24.419089
32	1.716	2020-02-05 20:43:31.169782
33	9.632	2020-02-05 20:43:49.926692
34	9.632	2020-02-05 21:00:15.948546
35	9.632	2020-02-05 21:02:11.507938
36	9.632	2020-02-05 21:02:24.321692
37	1.978	2020-02-05 21:06:02.900329
38	1.986	2020-02-05 21:06:31.421062
39	9.632	2020-02-05 21:06:47.985342
40	9.632	2020-02-05 21:12:23.289257
41	9.632	2020-02-05 21:12:48.170046
42	9.632	2020-02-05 21:19:14.383811
43	9.632	2020-02-05 21:20:34.546457
44	9.632	2020-02-05 21:20:52.796415
45	9.632	2020-02-05 21:21:05.984868
46	1.942	2020-02-05 21:57:09.324361
47	1.96	2020-02-05 21:57:31.237501
48	2.044	2020-02-05 21:58:01.173423
49	1.642	2020-02-05 21:58:31.149259
50	1.67	2020-02-05 21:59:01.438802
51	1.666	2020-02-05 21:59:31.114922
52	1.638	2020-02-05 22:00:01.246254
53	1.806	2020-02-05 22:00:31.164348
54	1.656	2020-02-05 22:01:01.177194
55	1.62	2020-02-05 22:01:31.120929
56	1.634	2020-02-05 22:02:01.407674
57	1.658	2020-02-05 22:02:31.343523
58	9.632	2020-02-05 22:40:38.936102
59	9.632	2020-02-05 22:43:05.268998
60	9.632	2020-02-05 22:43:41.13527
61	9.632	2020-02-05 22:44:01.579191
62	9.632	2020-02-05 22:45:18.161122
63	9.632	2020-02-05 22:50:10.753606
64	9.632	2020-02-05 22:50:26.903501
65	2.016	2020-02-05 22:56:31.520282
66	9.632	2020-02-05 23:20:54.731486
67	9.632	2020-02-05 23:21:26.360332
68	9.632	2020-02-06 20:31:28.326561
69	9.632	2020-02-06 20:32:19.437372
70	9.632	2020-02-06 21:17:45.552585
71	9.632	2020-02-06 21:21:39.354615
72	9.632	2020-02-06 21:21:52.259134
\.


--
-- Data for Name: kwhtotals; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kwhtotals (id, kwhtotal, ts) FROM stdin;
1	91.251	2020-02-05 19:27:16.613065
2	91.251	2020-02-05 19:27:31.421924
3	91.61	2020-02-05 19:30:08.64654
4	91.61	2020-02-05 19:30:31.252753
5	92.732	2020-02-05 19:41:29.953512
6	92.732	2020-02-05 19:41:31.250061
7	93.534	2020-02-05 19:44:42.451494
8	93.534	2020-02-05 19:45:05.238436
9	93.534	2020-02-05 19:45:31.206515
10	93.716	2020-02-05 19:46:01.221939
11	93.716	2020-02-05 19:46:31.130415
12	93.866	2020-02-05 19:47:01.59001
13	93.866	2020-02-05 19:47:31.878989
14	93.988	2020-02-05 19:48:01.697779
15	93.988	2020-02-05 19:48:32.429658
16	94.107	2020-02-05 19:49:04.665965
17	94.107	2020-02-05 19:49:31.387241
18	94.222	2020-02-05 19:50:01.512142
19	94.222	2020-02-05 19:50:31.416432
20	95.243	2020-02-05 19:59:06.590125
21	95.821	2020-02-05 20:07:34.586574
22	95.926	2020-02-05 20:09:29.854742
23	95.926	2020-02-05 20:09:31.151446
24	96.298	2020-02-05 20:15:46.27152
25	96.718	2020-02-05 20:23:36.379849
26	96.775	2020-02-05 20:23:54.19553
27	97.281	2020-02-05 20:31:31.532106
28	97.281	2020-02-05 20:31:31.699342
29	97.383	2020-02-05 20:31:47.528083
30	97.383	2020-02-05 20:31:57.992468
31	97.823	2020-02-05 20:43:24.426135
32	97.823	2020-02-05 20:43:31.175247
33	38.553	2020-02-05 20:43:49.931856
34	38.553	2020-02-05 21:00:15.953962
35	38.553	2020-02-05 21:02:11.513108
36	38.553	2020-02-05 21:02:24.326938
37	98.52	2020-02-05 21:06:02.905613
38	98.52	2020-02-05 21:06:31.436678
39	38.553	2020-02-05 21:06:47.990457
40	38.553	2020-02-05 21:12:23.295078
41	38.553	2020-02-05 21:12:48.175251
42	38.553	2020-02-05 21:19:14.389069
43	38.553	2020-02-05 21:20:34.551857
44	38.553	2020-02-05 21:20:52.801862
45	38.553	2020-02-05 21:21:05.990046
46	100.304	2020-02-05 21:57:09.339746
47	100.304	2020-02-05 21:57:31.242815
48	100.336	2020-02-05 21:58:01.178662
49	100.336	2020-02-05 21:58:31.154271
50	100.367	2020-02-05 21:59:01.447537
51	100.367	2020-02-05 21:59:31.120187
52	100.394	2020-02-05 22:00:01.252067
53	100.394	2020-02-05 22:00:31.169499
54	100.394	2020-02-05 22:01:01.182286
55	100.394	2020-02-05 22:01:31.126701
56	0.027	2020-02-05 22:02:01.412732
57	0.027	2020-02-05 22:02:31.34887
58	38.553	2020-02-05 22:40:38.942595
59	38.553	2020-02-05 22:43:05.274145
60	38.553	2020-02-05 22:43:41.140386
61	38.553	2020-02-05 22:44:01.584448
62	38.553	2020-02-05 22:45:18.166332
63	38.553	2020-02-05 22:50:10.759067
64	38.553	2020-02-05 22:50:26.908797
65	2.119	2020-02-05 22:56:31.529634
66	38.553	2020-02-05 23:20:54.736677
67	38.553	2020-02-05 23:21:26.366451
68	38.553	2020-02-06 20:31:28.331368
69	38.553	2020-02-06 20:32:19.442427
70	38.553	2020-02-06 21:17:45.558036
71	38.553	2020-02-06 21:21:39.359828
72	38.553	2020-02-06 21:21:52.264403
\.


--
-- Data for Name: kwhtotalsday; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kwhtotalsday (id, kwhtotal, ts) FROM stdin;
1	0	2020-02-05 19:27:06.482784
2	98.52	2020-02-05 21:06:13.107758
\.


--
-- Data for Name: kwhtotalsmonth; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kwhtotalsmonth (id, kwhtotal, ts) FROM stdin;
1	0	2020-02-05 19:27:06.482784
2	98.52	2020-02-05 21:06:13.126319
\.


--
-- Data for Name: pyteddbver; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pyteddbver (id, dbver, ts) FROM stdin;
1	0.4	2020-02-05 19:27:06.482784
2	0.5	2020-02-05 19:38:37.508158
\.


--
-- Data for Name: voltage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.voltage (id, voltage, ts) FROM stdin;
1	120.7	2020-02-05 19:27:16.599987
2	120.6	2020-02-05 19:27:31.409184
3	121.2	2020-02-05 19:30:08.632915
4	121.2	2020-02-05 19:30:31.240117
5	120.3	2020-02-05 19:41:29.942575
6	120.3	2020-02-05 19:41:31.156188
7	118.9	2020-02-05 19:44:42.439469
8	119.8	2020-02-05 19:45:05.221661
9	119.7	2020-02-05 19:45:31.195268
10	119.7	2020-02-05 19:46:01.210499
11	120.5	2020-02-05 19:46:31.119337
12	120.5	2020-02-05 19:47:01.577815
13	120.8	2020-02-05 19:47:31.867135
14	120.6	2020-02-05 19:48:01.68684
15	120.7	2020-02-05 19:48:32.417614
16	120.4	2020-02-05 19:49:04.65344
17	120.7	2020-02-05 19:49:31.376098
18	120.6	2020-02-05 19:50:01.50105
19	120.8	2020-02-05 19:50:31.405547
20	120.6	2020-02-05 19:59:06.576726
21	121.2	2020-02-05 20:07:34.567624
22	121.6	2020-02-05 20:09:29.842859
23	121.6	2020-02-05 20:09:31.139014
24	121.3	2020-02-05 20:15:46.259664
25	121.1	2020-02-05 20:23:36.368881
26	121.1	2020-02-05 20:23:54.183773
27	121	2020-02-05 20:31:31.52032
28	121	2020-02-05 20:31:31.686359
29	121.1	2020-02-05 20:31:47.516721
30	120.8	2020-02-05 20:31:57.980781
31	121.5	2020-02-05 20:43:24.408328
32	121.5	2020-02-05 20:43:31.163308
33	119.7	2020-02-05 20:43:49.920142
34	119.7	2020-02-05 21:00:15.942241
35	119.7	2020-02-05 21:02:11.501426
36	119.7	2020-02-05 21:02:24.315167
37	121.8	2020-02-05 21:06:02.893559
38	121.9	2020-02-05 21:06:31.405187
39	119.7	2020-02-05 21:06:47.978796
40	119.7	2020-02-05 21:12:23.282881
41	119.7	2020-02-05 21:12:48.16363
42	119.7	2020-02-05 21:19:14.377454
43	119.7	2020-02-05 21:20:34.540119
44	119.7	2020-02-05 21:20:52.789571
45	119.7	2020-02-05 21:21:05.978035
46	122.2	2020-02-05 21:57:09.315852
47	122	2020-02-05 21:57:31.231586
48	122.2	2020-02-05 21:58:01.167964
49	122.1	2020-02-05 21:58:31.142786
50	122.2	2020-02-05 21:59:01.430139
51	122.1	2020-02-05 21:59:31.10734
52	122.3	2020-02-05 22:00:01.239876
53	122.1	2020-02-05 22:00:31.158423
54	122.2	2020-02-05 22:01:01.171118
55	122.3	2020-02-05 22:01:31.113872
56	122.2	2020-02-05 22:02:01.401395
57	122.5	2020-02-05 22:02:31.336975
58	119.7	2020-02-05 22:40:38.925395
59	119.7	2020-02-05 22:43:05.261995
60	119.7	2020-02-05 22:43:41.129104
61	119.7	2020-02-05 22:44:01.572746
62	119.7	2020-02-05 22:45:18.154827
63	119.7	2020-02-05 22:50:10.747107
64	119.7	2020-02-05 22:50:26.897188
65	120.4	2020-02-05 22:56:31.493244
66	119.7	2020-02-05 23:20:54.725211
67	119.7	2020-02-05 23:21:26.351562
68	119.7	2020-02-06 20:31:28.31504
69	119.7	2020-02-06 20:32:19.431131
70	119.7	2020-02-06 21:17:45.546173
71	119.7	2020-02-06 21:21:39.348089
72	119.7	2020-02-06 21:21:52.252633
\.


--
-- Name: killawatts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.killawatts_id_seq', 72, true);


--
-- Name: kwhtotals_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kwhtotals_id_seq', 72, true);


--
-- Name: kwhtotalsday_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kwhtotalsday_id_seq', 2, true);


--
-- Name: kwhtotalsmonth_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kwhtotalsmonth_id_seq', 2, true);


--
-- Name: pyteddbver_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pyteddbver_id_seq', 2, true);


--
-- Name: voltage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.voltage_id_seq', 72, true);


--
-- Name: killawatts killawatts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.killawatts
    ADD CONSTRAINT killawatts_pkey PRIMARY KEY (id);


--
-- Name: kwhtotals kwhtotals_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kwhtotals
    ADD CONSTRAINT kwhtotals_pkey PRIMARY KEY (id);


--
-- Name: kwhtotalsday kwhtotalsday_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kwhtotalsday
    ADD CONSTRAINT kwhtotalsday_pkey PRIMARY KEY (id);


--
-- Name: kwhtotalsmonth kwhtotalsmonth_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kwhtotalsmonth
    ADD CONSTRAINT kwhtotalsmonth_pkey PRIMARY KEY (id);


--
-- Name: pyteddbver pyteddbver_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pyteddbver
    ADD CONSTRAINT pyteddbver_pkey PRIMARY KEY (id);


--
-- Name: voltage voltage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voltage
    ADD CONSTRAINT voltage_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

