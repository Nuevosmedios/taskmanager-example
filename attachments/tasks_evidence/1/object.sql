set search_path = 'meti';

BEGIN;
CREATE TABLE "object_permissions_section_perms" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "obj_id" integer NOT NULL REFERENCES "sections_section" ("id") DEFERRABLE INITIALLY DEFERRED,
    "edit" integer NOT NULL,
    "destroy" integer NOT NULL,
    "see_corrections" integer NOT NULL,
    "copy" integer NOT NULL,
    "view" integer NOT NULL
)
;
CREATE TABLE "object_permissions_versiondiagnostic_perms" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "obj_id" integer NOT NULL REFERENCES "autodiagnostic_versiondiagnostic" ("id") DEFERRABLE INITIALLY DEFERRED,
    "edit" integer NOT NULL,
    "destroy" integer NOT NULL,
    "create_session" integer NOT NULL,
    "view" integer NOT NULL
)
;
CREATE TABLE "object_permissions_sectioninmodule_perms" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "obj_id" integer NOT NULL REFERENCES "autodiagnostic_sectioninmodule" ("id") DEFERRABLE INITIALLY DEFERRED,
    "see_corrections" integer NOT NULL
)
;
CREATE TABLE "object_permissions_content_perms" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "obj_id" integer NOT NULL REFERENCES "content_content" ("id") DEFERRABLE INITIALLY DEFERRED,
    "edit" integer NOT NULL,
    "destroy" integer NOT NULL,
    "see_corrections" integer NOT NULL,
    "copy" integer NOT NULL,
    "view" integer NOT NULL
)
;
CREATE TABLE "object_permissions_question_perms" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "obj_id" integer NOT NULL REFERENCES "content_question" ("id") DEFERRABLE INITIALLY DEFERRED,
    "edit" integer NOT NULL,
    "copy" integer NOT NULL,
    "view" integer NOT NULL
)
;
CREATE TABLE "object_permissions_versioncourse_perms" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "obj_id" integer NOT NULL REFERENCES "lms_versioncourse" ("id") DEFERRABLE INITIALLY DEFERRED,
    "edit" integer NOT NULL,
    "destroy" integer NOT NULL,
    "create_session" integer NOT NULL,
    "view" integer NOT NULL
)
;
CREATE TABLE "object_permissions_contentinmodule_perms" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "obj_id" integer NOT NULL REFERENCES "lms_contentinmodule" ("id") DEFERRABLE INITIALLY DEFERRED,
    "see_corrections" integer NOT NULL
)
;
CREATE TABLE "object_permissions_group_perms" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "obj_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "admin" integer NOT NULL
)
;
CREATE INDEX "object_permissions_section_perms_user_id" ON "object_permissions_section_perms" ("user_id");
CREATE INDEX "object_permissions_section_perms_group_id" ON "object_permissions_section_perms" ("group_id");
CREATE INDEX "object_permissions_section_perms_obj_id" ON "object_permissions_section_perms" ("obj_id");
CREATE INDEX "object_permissions_versiondiagnostic_perms_user_id" ON "object_permissions_versiondiagnostic_perms" ("user_id");
CREATE INDEX "object_permissions_versiondiagnostic_perms_group_id" ON "object_permissions_versiondiagnostic_perms" ("group_id");
CREATE INDEX "object_permissions_versiondiagnostic_perms_obj_id" ON "object_permissions_versiondiagnostic_perms" ("obj_id");
CREATE INDEX "object_permissions_sectioninmodule_perms_user_id" ON "object_permissions_sectioninmodule_perms" ("user_id");
CREATE INDEX "object_permissions_sectioninmodule_perms_group_id" ON "object_permissions_sectioninmodule_perms" ("group_id");
CREATE INDEX "object_permissions_sectioninmodule_perms_obj_id" ON "object_permissions_sectioninmodule_perms" ("obj_id");
CREATE INDEX "object_permissions_content_perms_user_id" ON "object_permissions_content_perms" ("user_id");
CREATE INDEX "object_permissions_content_perms_group_id" ON "object_permissions_content_perms" ("group_id");
CREATE INDEX "object_permissions_content_perms_obj_id" ON "object_permissions_content_perms" ("obj_id");
CREATE INDEX "object_permissions_question_perms_user_id" ON "object_permissions_question_perms" ("user_id");
CREATE INDEX "object_permissions_question_perms_group_id" ON "object_permissions_question_perms" ("group_id");
CREATE INDEX "object_permissions_question_perms_obj_id" ON "object_permissions_question_perms" ("obj_id");
CREATE INDEX "object_permissions_versioncourse_perms_user_id" ON "object_permissions_versioncourse_perms" ("user_id");
CREATE INDEX "object_permissions_versioncourse_perms_group_id" ON "object_permissions_versioncourse_perms" ("group_id");
CREATE INDEX "object_permissions_versioncourse_perms_obj_id" ON "object_permissions_versioncourse_perms" ("obj_id");
CREATE INDEX "object_permissions_contentinmodule_perms_user_id" ON "object_permissions_contentinmodule_perms" ("user_id");
CREATE INDEX "object_permissions_contentinmodule_perms_group_id" ON "object_permissions_contentinmodule_perms" ("group_id");
CREATE INDEX "object_permissions_contentinmodule_perms_obj_id" ON "object_permissions_contentinmodule_perms" ("obj_id");
CREATE INDEX "object_permissions_group_perms_user_id" ON "object_permissions_group_perms" ("user_id");
CREATE INDEX "object_permissions_group_perms_group_id" ON "object_permissions_group_perms" ("group_id");
CREATE INDEX "object_permissions_group_perms_obj_id" ON "object_permissions_group_perms" ("obj_id");

COMMIT;
