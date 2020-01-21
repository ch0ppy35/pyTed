--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4 (Debian 10.4-2.pgdg90+1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

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

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: killawatts; Type: TABLE; Schema: public; Owner: postgresadmin
--

CREATE TABLE public.killawatts (
    id integer NOT NULL,
    killawatts real,
    ts timestamp without time zone DEFAULT now()
);


ALTER TABLE public.killawatts OWNER TO postgresadmin;

--
-- Name: killawatts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresadmin
--

CREATE SEQUENCE public.killawatts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.killawatts_id_seq OWNER TO postgresadmin;

--
-- Name: killawatts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgresadmin
--

ALTER SEQUENCE public.killawatts_id_seq OWNED BY public.killawatts.id;


--
-- Name: kwhtotals; Type: TABLE; Schema: public; Owner: postgresadmin
--

CREATE TABLE public.kwhtotals (
    id integer NOT NULL,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.kwhtotals OWNER TO postgresadmin;

--
-- Name: kwhtotals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresadmin
--

CREATE SEQUENCE public.kwhtotals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kwhtotals_id_seq OWNER TO postgresadmin;

--
-- Name: kwhtotals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgresadmin
--

ALTER SEQUENCE public.kwhtotals_id_seq OWNED BY public.kwhtotals.id;


--
-- Name: kwhtotalsday; Type: TABLE; Schema: public; Owner: postgresadmin
--

CREATE TABLE public.kwhtotalsday (
    id integer NOT NULL,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.kwhtotalsday OWNER TO postgresadmin;

--
-- Name: kwhtotalsday_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresadmin
--

CREATE SEQUENCE public.kwhtotalsday_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kwhtotalsday_id_seq OWNER TO postgresadmin;

--
-- Name: kwhtotalsday_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgresadmin
--

ALTER SEQUENCE public.kwhtotalsday_id_seq OWNED BY public.kwhtotalsday.id;


--
-- Name: kwhtotalsmonth; Type: TABLE; Schema: public; Owner: postgresadmin
--

CREATE TABLE public.kwhtotalsmonth (
    id integer NOT NULL,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.kwhtotalsmonth OWNER TO postgresadmin;

--
-- Name: kwhtotalsmonth_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresadmin
--

CREATE SEQUENCE public.kwhtotalsmonth_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kwhtotalsmonth_id_seq OWNER TO postgresadmin;

--
-- Name: kwhtotalsmonth_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgresadmin
--

ALTER SEQUENCE public.kwhtotalsmonth_id_seq OWNED BY public.kwhtotalsmonth.id;


--
-- Name: kwhtotalsweek; Type: TABLE; Schema: public; Owner: postgresadmin
--

CREATE TABLE public.kwhtotalsweek (
    id integer NOT NULL,
    kwhtotal real NOT NULL,
    ts timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.kwhtotalsweek OWNER TO postgresadmin;

--
-- Name: kwhtotalsweek_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresadmin
--

CREATE SEQUENCE public.kwhtotalsweek_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kwhtotalsweek_id_seq OWNER TO postgresadmin;

--
-- Name: kwhtotalsweek_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgresadmin
--

ALTER SEQUENCE public.kwhtotalsweek_id_seq OWNED BY public.kwhtotalsweek.id;


--
-- Name: voltage; Type: TABLE; Schema: public; Owner: postgresadmin
--

CREATE TABLE public.voltage (
    id integer NOT NULL,
    voltage real,
    ts timestamp without time zone DEFAULT now()
);


ALTER TABLE public.voltage OWNER TO postgresadmin;

--
-- Name: voltage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgresadmin
--

CREATE SEQUENCE public.voltage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voltage_id_seq OWNER TO postgresadmin;

--
-- Name: voltage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgresadmin
--

ALTER SEQUENCE public.voltage_id_seq OWNED BY public.voltage.id;


--
-- Name: killawatts id; Type: DEFAULT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.killawatts ALTER COLUMN id SET DEFAULT nextval('public.killawatts_id_seq'::regclass);


--
-- Name: kwhtotals id; Type: DEFAULT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.kwhtotals ALTER COLUMN id SET DEFAULT nextval('public.kwhtotals_id_seq'::regclass);


--
-- Name: kwhtotalsday id; Type: DEFAULT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.kwhtotalsday ALTER COLUMN id SET DEFAULT nextval('public.kwhtotalsday_id_seq'::regclass);


--
-- Name: kwhtotalsmonth id; Type: DEFAULT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.kwhtotalsmonth ALTER COLUMN id SET DEFAULT nextval('public.kwhtotalsmonth_id_seq'::regclass);


--
-- Name: kwhtotalsweek id; Type: DEFAULT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.kwhtotalsweek ALTER COLUMN id SET DEFAULT nextval('public.kwhtotalsweek_id_seq'::regclass);


--
-- Name: voltage id; Type: DEFAULT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.voltage ALTER COLUMN id SET DEFAULT nextval('public.voltage_id_seq'::regclass);


--
-- Name: killawatts killawatts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.killawatts
    ADD CONSTRAINT killawatts_pkey PRIMARY KEY (id);


--
-- Name: kwhtotals kwhtotals_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.kwhtotals
    ADD CONSTRAINT kwhtotals_pkey PRIMARY KEY (id);


--
-- Name: kwhtotalsday kwhtotalsday_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.kwhtotalsday
    ADD CONSTRAINT kwhtotalsday_pkey PRIMARY KEY (id);


--
-- Name: kwhtotalsmonth kwhtotalsmonth_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.kwhtotalsmonth
    ADD CONSTRAINT kwhtotalsmonth_pkey PRIMARY KEY (id);


--
-- Name: kwhtotalsweek kwhtotalsweek_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.kwhtotalsweek
    ADD CONSTRAINT kwhtotalsweek_pkey PRIMARY KEY (id);


--
-- Name: voltage voltage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgresadmin
--

ALTER TABLE ONLY public.voltage
    ADD CONSTRAINT voltage_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

