PGDMP                          {            postgres    15.1    15.1 )    ,           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            -           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            .           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            /           1262    5    postgres    DATABASE     |   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE postgres;
                postgres    false            0           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3375                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            1           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            ?            1259    16456    project    TABLE     ?   CREATE TABLE public.project (
    id_project integer NOT NULL,
    name character varying NOT NULL,
    "desc" text,
    date_start date NOT NULL,
    date_duration integer NOT NULL,
    date_end date NOT NULL,
    id_task integer NOT NULL
);
    DROP TABLE public.project;
       public         heap    postgres    false            ?            1259    16455    project_id_project_seq    SEQUENCE     ?   ALTER TABLE public.project ALTER COLUMN id_project ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.project_id_project_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    224            ?            1259    16428    role    TABLE     e   CREATE TABLE public.role (
    id_role integer NOT NULL,
    name_role character varying NOT NULL
);
    DROP TABLE public.role;
       public         heap    postgres    false            ?            1259    16427    role_id_role_seq    SEQUENCE     ?   ALTER TABLE public.role ALTER COLUMN id_role ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.role_id_role_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    222            ?            1259    16398    task    TABLE     ?   CREATE TABLE public.task (
    id_task integer NOT NULL,
    name character varying NOT NULL,
    desk text,
    date_start date NOT NULL,
    date_duration integer NOT NULL,
    date_end date NOT NULL
);
    DROP TABLE public.task;
       public         heap    postgres    false            ?            1259    16412 	   task2task    TABLE     a   CREATE TABLE public.task2task (
    id_task integer NOT NULL,
    id_subtask integer NOT NULL
);
    DROP TABLE public.task2task;
       public         heap    postgres    false            ?            1259    16423    task_id_task_seq    SEQUENCE     ?   ALTER TABLE public.task ALTER COLUMN id_task ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.task_id_task_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215            ?            1259    16468    user2project    TABLE     ?   CREATE TABLE public.user2project (
    id_user integer NOT NULL,
    id_project integer NOT NULL,
    id_role integer NOT NULL
);
     DROP TABLE public.user2project;
       public         heap    postgres    false            ?            1259    16424 	   user2task    TABLE     |   CREATE TABLE public.user2task (
    id_user integer NOT NULL,
    id_task integer NOT NULL,
    id_role integer NOT NULL
);
    DROP TABLE public.user2task;
       public         heap    postgres    false            ?            1259    16405    users    TABLE     ?   CREATE TABLE public.users (
    id_user integer NOT NULL,
    name character varying NOT NULL,
    password character varying NOT NULL,
    email character varying NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            ?            1259    16422    users_id_user_seq    SEQUENCE     ?   ALTER TABLE public.users ALTER COLUMN id_user ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_user_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    216            (          0    16456    project 
   TABLE DATA           i   COPY public.project (id_project, name, "desc", date_start, date_duration, date_end, id_task) FROM stdin;
    public          postgres    false    224   N.       &          0    16428    role 
   TABLE DATA           2   COPY public.role (id_role, name_role) FROM stdin;
    public          postgres    false    222   k.                 0    16398    task 
   TABLE DATA           X   COPY public.task (id_task, name, desk, date_start, date_duration, date_end) FROM stdin;
    public          postgres    false    215   ?.       !          0    16412 	   task2task 
   TABLE DATA           8   COPY public.task2task (id_task, id_subtask) FROM stdin;
    public          postgres    false    217   F/       )          0    16468    user2project 
   TABLE DATA           D   COPY public.user2project (id_user, id_project, id_role) FROM stdin;
    public          postgres    false    225   c/       $          0    16424 	   user2task 
   TABLE DATA           >   COPY public.user2task (id_user, id_task, id_role) FROM stdin;
    public          postgres    false    220   ?/                  0    16405    users 
   TABLE DATA           ?   COPY public.users (id_user, name, password, email) FROM stdin;
    public          postgres    false    216   ?/       2           0    0    project_id_project_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.project_id_project_seq', 1, false);
          public          postgres    false    223            3           0    0    role_id_role_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.role_id_role_seq', 2, true);
          public          postgres    false    221            4           0    0    task_id_task_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.task_id_task_seq', 2, true);
          public          postgres    false    219            5           0    0    users_id_user_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.users_id_user_seq', 3, true);
          public          postgres    false    218            ?           2606    16462    project project_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id_project);
 >   ALTER TABLE ONLY public.project DROP CONSTRAINT project_pkey;
       public            postgres    false    224            ?           2606    16434    role role_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (id_role);
 8   ALTER TABLE ONLY public.role DROP CONSTRAINT role_pkey;
       public            postgres    false    222            ?           2606    16404    task task_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (id_task);
 8   ALTER TABLE ONLY public.task DROP CONSTRAINT task_pkey;
       public            postgres    false    215            ?           2606    16411    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id_user);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    216            ?           2606    16476 ,   user2project project2project_id_project_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.user2project
    ADD CONSTRAINT project2project_id_project_fkey FOREIGN KEY (id_project) REFERENCES public.project(id_project);
 V   ALTER TABLE ONLY public.user2project DROP CONSTRAINT project2project_id_project_fkey;
       public          postgres    false    225    224    3208            ?           2606    16481 )   user2project project2project_id_role_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.user2project
    ADD CONSTRAINT project2project_id_role_fkey FOREIGN KEY (id_role) REFERENCES public.role(id_role);
 S   ALTER TABLE ONLY public.user2project DROP CONSTRAINT project2project_id_role_fkey;
       public          postgres    false    222    225    3206            ?           2606    16471 )   user2project project2project_id_user_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.user2project
    ADD CONSTRAINT project2project_id_user_fkey FOREIGN KEY (id_user) REFERENCES public.users(id_user);
 S   ALTER TABLE ONLY public.user2project DROP CONSTRAINT project2project_id_user_fkey;
       public          postgres    false    216    225    3204            ?           2606    16463    project project_id_task_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.project
    ADD CONSTRAINT project_id_task_fkey FOREIGN KEY (id_task) REFERENCES public.task(id_task) NOT VALID;
 F   ALTER TABLE ONLY public.project DROP CONSTRAINT project_id_task_fkey;
       public          postgres    false    3202    215    224            ?           2606    16435     task2task task2task_id_task_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.task2task
    ADD CONSTRAINT task2task_id_task_fkey FOREIGN KEY (id_task) REFERENCES public.task(id_task) NOT VALID;
 J   ALTER TABLE ONLY public.task2task DROP CONSTRAINT task2task_id_task_fkey;
       public          postgres    false    3202    217    215            ?           2606    16450     user2task user2task_id_role_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.user2task
    ADD CONSTRAINT user2task_id_role_fkey FOREIGN KEY (id_role) REFERENCES public.role(id_role) NOT VALID;
 J   ALTER TABLE ONLY public.user2task DROP CONSTRAINT user2task_id_role_fkey;
       public          postgres    false    222    3206    220            ?           2606    16445     user2task user2task_id_task_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.user2task
    ADD CONSTRAINT user2task_id_task_fkey FOREIGN KEY (id_task) REFERENCES public.task(id_task) NOT VALID;
 J   ALTER TABLE ONLY public.user2task DROP CONSTRAINT user2task_id_task_fkey;
       public          postgres    false    220    3202    215            ?           2606    16440     user2task user2task_id_user_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.user2task
    ADD CONSTRAINT user2task_id_user_fkey FOREIGN KEY (id_user) REFERENCES public.users(id_user) NOT VALID;
 J   ALTER TABLE ONLY public.user2task DROP CONSTRAINT user2task_id_user_fkey;
       public          postgres    false    3204    220    216            (      x?????? ? ?      &   7   x?3估?b????]?}a/??ta???{??8/,??|aPboA?????? :?#A         ?   x?3估?¾?.6_츰?b??N w?ņ[/l??@??)\?{???6]??????????9???ˈ??|?Y???????ya??@s?u.?
nZ?AlT?Pd???^???c???=... pvf?      !      x?????? ? ?      )      x?????? ? ?      $      x?3?4?4?2?F\Ɯ@?+F??? !}?          8   x?3?N̫L?446672??LL?OJt?M???+*?2?????7??㐏???? z??     