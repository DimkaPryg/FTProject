CREATE TABLE public.article_types (id serial4 NOT NULL, "type" varchar NULL,CONSTRAINT article_types_pkey PRIMARY KEY (id));
CREATE INDEX ix_article_types_id ON public.article_types USING btree (id);


CREATE TABLE public.author (id serial4 NOT NULL,author varchar NULL,CONSTRAINT author_pkey PRIMARY KEY (id));
CREATE INDEX ix_author_id ON public.author USING btree (id);


CREATE TABLE public.magazines (id serial4 NOT NULL,"name" varchar NULL,CONSTRAINT magazines_pkey PRIMARY KEY (id));
CREATE INDEX ix_magazines_id ON public.magazines USING btree (id);

CREATE TABLE public.articles (id serial4 NOT NULL,magazine_id int4 NULL,article_type_id int4 NULL,author_id int4 NULL,CONSTRAINT articles_pkey PRIMARY KEY (id));
CREATE INDEX ix_articles_id ON public.articles USING btree (id);

ALTER TABLE public.articles ADD CONSTRAINT articles_article_type_id_fkey FOREIGN KEY (article_type_id) REFERENCES public.article_types(id);
ALTER TABLE public.articles ADD CONSTRAINT articles_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.author(id);
ALTER TABLE public.articles ADD CONSTRAINT articles_magazine_id_fkey FOREIGN KEY (magazine_id) REFERENCES public.magazines(id);

INSERT INTO public.article_types (id, "type") VALUES(1, 'news');
INSERT INTO public.article_types (id, "type") VALUES(2, 'tech');
INSERT INTO public.article_types (id, "type") VALUES(3, 'entertainment');

INSERT INTO public.author (id, author) VALUES(1, 'Chappie');
INSERT INTO public.author (id, author) VALUES(2, 'Wall-e');
INSERT INTO public.author (id, author) VALUES(3, 'Atom');
INSERT INTO public.author (id, author) VALUES(4, 'T1000');

INSERT INTO public.magazines (id, "name") VALUES(1, 'it herald');
INSERT INTO public.magazines (id, "name") VALUES(2, 'IT STORIES');
INSERT INTO public.magazines (id, "name") VALUES(3, 'IT with kids');

INSERT INTO public.articles (id, magazine_id, article_type_id, author_id) VALUES(1, 1, 2, 3);
INSERT INTO public.articles (id, magazine_id, article_type_id, author_id) VALUES(2, 3, 3, 2);
INSERT INTO public.articles (id, magazine_id, article_type_id, author_id) VALUES(3, 2, 2, 4);
INSERT INTO public.articles (id, magazine_id, article_type_id, author_id) VALUES(4, 1, 1, 1);
