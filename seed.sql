--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

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
-- Name: bookgenres; Type: TABLE; Schema: public; Owner: antikiller
--

CREATE TABLE public.bookgenres (
    bookgenre_id integer NOT NULL,
    book_id integer,
    genre_id integer
);


ALTER TABLE public.bookgenres OWNER TO antikiller;

--
-- Name: bookgenres_bookgenre_id_seq; Type: SEQUENCE; Schema: public; Owner: antikiller
--

CREATE SEQUENCE public.bookgenres_bookgenre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bookgenres_bookgenre_id_seq OWNER TO antikiller;

--
-- Name: bookgenres_bookgenre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: antikiller
--

ALTER SEQUENCE public.bookgenres_bookgenre_id_seq OWNED BY public.bookgenres.bookgenre_id;


--
-- Name: books; Type: TABLE; Schema: public; Owner: antikiller
--

CREATE TABLE public.books (
    book_id integer NOT NULL,
    title character varying,
    author character varying,
    published_date timestamp without time zone,
    description character varying
);


ALTER TABLE public.books OWNER TO antikiller;

--
-- Name: books_book_id_seq; Type: SEQUENCE; Schema: public; Owner: antikiller
--

CREATE SEQUENCE public.books_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_book_id_seq OWNER TO antikiller;

--
-- Name: books_book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: antikiller
--

ALTER SEQUENCE public.books_book_id_seq OWNED BY public.books.book_id;


--
-- Name: books_to_read; Type: TABLE; Schema: public; Owner: antikiller
--

CREATE TABLE public.books_to_read (
    book_to_read_id integer NOT NULL,
    book_id integer,
    user_id integer
);


ALTER TABLE public.books_to_read OWNER TO antikiller;

--
-- Name: books_to_read_book_to_read_id_seq; Type: SEQUENCE; Schema: public; Owner: antikiller
--

CREATE SEQUENCE public.books_to_read_book_to_read_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_to_read_book_to_read_id_seq OWNER TO antikiller;

--
-- Name: books_to_read_book_to_read_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: antikiller
--

ALTER SEQUENCE public.books_to_read_book_to_read_id_seq OWNED BY public.books_to_read.book_to_read_id;


--
-- Name: genres; Type: TABLE; Schema: public; Owner: antikiller
--

CREATE TABLE public.genres (
    genre_id integer NOT NULL,
    genre character varying
);


ALTER TABLE public.genres OWNER TO antikiller;

--
-- Name: genres_genre_id_seq; Type: SEQUENCE; Schema: public; Owner: antikiller
--

CREATE SEQUENCE public.genres_genre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genres_genre_id_seq OWNER TO antikiller;

--
-- Name: genres_genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: antikiller
--

ALTER SEQUENCE public.genres_genre_id_seq OWNED BY public.genres.genre_id;


--
-- Name: reviews; Type: TABLE; Schema: public; Owner: antikiller
--

CREATE TABLE public.reviews (
    review_id integer NOT NULL,
    rating integer,
    text_review integer,
    created_date timestamp without time zone,
    book_id integer,
    user_id integer
);


ALTER TABLE public.reviews OWNER TO antikiller;

--
-- Name: reviews_review_id_seq; Type: SEQUENCE; Schema: public; Owner: antikiller
--

CREATE SEQUENCE public.reviews_review_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reviews_review_id_seq OWNER TO antikiller;

--
-- Name: reviews_review_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: antikiller
--

ALTER SEQUENCE public.reviews_review_id_seq OWNED BY public.reviews.review_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: antikiller
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL,
    nickname character varying,
    user_picture character varying,
    zipcode integer
);


ALTER TABLE public.users OWNER TO antikiller;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: antikiller
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO antikiller;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: antikiller
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: bookgenres bookgenre_id; Type: DEFAULT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.bookgenres ALTER COLUMN bookgenre_id SET DEFAULT nextval('public.bookgenres_bookgenre_id_seq'::regclass);


--
-- Name: books book_id; Type: DEFAULT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.books ALTER COLUMN book_id SET DEFAULT nextval('public.books_book_id_seq'::regclass);


--
-- Name: books_to_read book_to_read_id; Type: DEFAULT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.books_to_read ALTER COLUMN book_to_read_id SET DEFAULT nextval('public.books_to_read_book_to_read_id_seq'::regclass);


--
-- Name: genres genre_id; Type: DEFAULT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.genres ALTER COLUMN genre_id SET DEFAULT nextval('public.genres_genre_id_seq'::regclass);


--
-- Name: reviews review_id; Type: DEFAULT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.reviews ALTER COLUMN review_id SET DEFAULT nextval('public.reviews_review_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: bookgenres; Type: TABLE DATA; Schema: public; Owner: antikiller
--

COPY public.bookgenres (bookgenre_id, book_id, genre_id) FROM stdin;
\.


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: antikiller
--

COPY public.books (book_id, title, author, published_date, description) FROM stdin;
\.


--
-- Data for Name: books_to_read; Type: TABLE DATA; Schema: public; Owner: antikiller
--

COPY public.books_to_read (book_to_read_id, book_id, user_id) FROM stdin;
\.


--
-- Data for Name: genres; Type: TABLE DATA; Schema: public; Owner: antikiller
--

COPY public.genres (genre_id, genre) FROM stdin;
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: antikiller
--

COPY public.reviews (review_id, rating, text_review, created_date, book_id, user_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: antikiller
--

COPY public.users (user_id, email, password, nickname, user_picture, zipcode) FROM stdin;
1	test@test.test	test	\N	\N	\N
4	test2@test.test	test	\N	\N	\N
\.


--
-- Name: bookgenres_bookgenre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: antikiller
--

SELECT pg_catalog.setval('public.bookgenres_bookgenre_id_seq', 1, false);


--
-- Name: books_book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: antikiller
--

SELECT pg_catalog.setval('public.books_book_id_seq', 1, false);


--
-- Name: books_to_read_book_to_read_id_seq; Type: SEQUENCE SET; Schema: public; Owner: antikiller
--

SELECT pg_catalog.setval('public.books_to_read_book_to_read_id_seq', 1, false);


--
-- Name: genres_genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: antikiller
--

SELECT pg_catalog.setval('public.genres_genre_id_seq', 1, false);


--
-- Name: reviews_review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: antikiller
--

SELECT pg_catalog.setval('public.reviews_review_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: antikiller
--

SELECT pg_catalog.setval('public.users_user_id_seq', 4, true);


--
-- Name: bookgenres bookgenres_pkey; Type: CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.bookgenres
    ADD CONSTRAINT bookgenres_pkey PRIMARY KEY (bookgenre_id);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (book_id);


--
-- Name: books_to_read books_to_read_pkey; Type: CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.books_to_read
    ADD CONSTRAINT books_to_read_pkey PRIMARY KEY (book_to_read_id);


--
-- Name: genres genres_pkey; Type: CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (genre_id);


--
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (review_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: bookgenres bookgenres_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.bookgenres
    ADD CONSTRAINT bookgenres_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(book_id);


--
-- Name: bookgenres bookgenres_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.bookgenres
    ADD CONSTRAINT bookgenres_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public.genres(genre_id);


--
-- Name: books_to_read books_to_read_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.books_to_read
    ADD CONSTRAINT books_to_read_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(book_id);


--
-- Name: books_to_read books_to_read_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.books_to_read
    ADD CONSTRAINT books_to_read_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: reviews reviews_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(book_id);


--
-- Name: reviews reviews_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: antikiller
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

