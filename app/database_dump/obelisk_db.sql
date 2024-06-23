--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Ubuntu 16.3-1.pgdg22.04+1)
-- Dumped by pg_dump version 16.3 (Ubuntu 16.3-1.pgdg22.04+1)

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
-- Name: dex_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dex_user (
    telegram_id text NOT NULL,
    wallet_address text NOT NULL,
    points integer,
    referral_code text NOT NULL,
    claimed_code text NOT NULL
);


ALTER TABLE public.dex_user OWNER TO postgres;

--
-- Name: social_links; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.social_links (
    telegram_id text NOT NULL,
    site_link text,
    twitter_link text,
    telegram_link text,
    discord_link text
);


ALTER TABLE public.social_links OWNER TO postgres;

--
-- Name: transactions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transactions (
    telegram_id text NOT NULL,
    market text NOT NULL,
    type text NOT NULL,
    side text NOT NULL,
    amount integer NOT NULL,
    price double precision NOT NULL,
    "timestamp" timestamp without time zone NOT NULL
);


ALTER TABLE public.transactions OWNER TO postgres;

--
-- Data for Name: dex_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dex_user (telegram_id, wallet_address, points, referral_code, claimed_code) FROM stdin;
		0	obelisk-u0RefLqTdAlpW6z5	
user123	0xabc...	0	obelisk-ZKsTMVlyf4p4QZhL	claim456
\.


--
-- Data for Name: social_links; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.social_links (telegram_id, site_link, twitter_link, telegram_link, discord_link) FROM stdin;
\.


--
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transactions (telegram_id, market, type, side, amount, price, "timestamp") FROM stdin;
\.


--
-- Name: dex_user dex_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dex_user
    ADD CONSTRAINT dex_user_pkey PRIMARY KEY (telegram_id);


--
-- Name: social_links social_links_telegram_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.social_links
    ADD CONSTRAINT social_links_telegram_id_fkey FOREIGN KEY (telegram_id) REFERENCES public.dex_user(telegram_id);


--
-- Name: transactions transactions_telegram_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_telegram_id_fkey FOREIGN KEY (telegram_id) REFERENCES public.dex_user(telegram_id);


--
-- Name: TABLE dex_user; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.dex_user TO obelisk_dex_admin;


--
-- Name: TABLE social_links; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.social_links TO obelisk_dex_admin;


--
-- Name: TABLE transactions; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.transactions TO obelisk_dex_admin;


--
-- PostgreSQL database dump complete
--

