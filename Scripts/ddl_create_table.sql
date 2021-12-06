-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Property" (
    "listing_id" INTEGER   NOT NULL,
    "host_id" INTEGER   NOT NULL,
    "listing_url" VARCHAR   NOT NULL,
    "name" VARCHAR   NOT NULL,
    "property_type" VARCHAR   NOT NULL,
    "room_type" VARCHAR   NOT NULL,
    "accommodates" INTEGER   NOT NULL,
    "bathrooms" NUMERIC   NOT NULL,
    "bedrooms" INTEGER   NOT NULL,
    "beds" INTEGER   NOT NULL,
    "bed_type" VARCHAR   NOT NULL,
    "square_feet" NUMERIC   NOT NULL,
    "description" VARCHAR   NOT NULL,
    "notes" VARCHAR   NOT NULL,
    "transit" VARCHAR   NOT NULL,
    "picture_url" VARCHAR   NOT NULL,
    "guests_included" INTEGER   NOT NULL,
    "minimum_nights" INTEGER   NOT NULL,
    "maximum_nights" INTEGER   NOT NULL,
    CONSTRAINT "pk_Property" PRIMARY KEY (
        "listing_id"
     )
);

CREATE TABLE "Host" (
    "host_id" INTEGER   NOT NULL,
    "host_url" VARCHAR   NOT NULL,
    "host_name" VARCHAR   NOT NULL,
    "host_since" DATE   NOT NULL,
    "host_about" VARCHAR   NOT NULL,
    "host_is_superhost" BOOLEAN   NOT NULL,
    "host_picture_url" VARCHAR   NOT NULL,
    "host_listings_count" INTEGER   NOT NULL,
    "host_identity_verified" BOOLEAN   NOT NULL,
    "host_location" VARCHAR   NOT NULL,
    "host_response_time" VARCHAR   NOT NULL,
    "host_response_rate" INTEGER   NOT NULL,
    "host_acceptance_rate" INTEGER   NOT NULL,
    "host_neighbourhood" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Host" PRIMARY KEY (
        "host_id"
     )
);

CREATE TABLE "Host_Verifications" (
    "host_id" INTEGER   NOT NULL,
    "host_verifications" VARCHAR   NOT NULL
);

CREATE TABLE "Address" (
    "listing_id" INTEGER   NOT NULL,
    "country_code" VARCHAR   NOT NULL,
    "country" VARCHAR   NOT NULL,
    "state" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    "zipcode" INTEGER   NOT NULL,
    "smart_location" VARCHAR   NOT NULL,
    "neighbourhood" VARCHAR   NOT NULL,
    "street" VARCHAR   NOT NULL,
    "latitude" NUMERIC   NOT NULL,
    "longitude" NUMERIC   NOT NULL,
    "is_location_exact" BOOLEAN   NOT NULL,
    CONSTRAINT "pk_Address" PRIMARY KEY (
        "listing_id"
     )
);

CREATE TABLE "Amenities" (
    "listing_id" INTEGER   NOT NULL,
    "amenities" VARCHAR   NOT NULL
);

CREATE TABLE "Availability" (
    "listing_id" INTEGER   NOT NULL,
    "has_availability" BOOLEAN   NOT NULL,
    "availability_30" INTEGER   NOT NULL,
    "availability_60" INTEGER   NOT NULL,
    "availability_90" INTEGER   NOT NULL,
    "availability_365" INTEGER   NOT NULL,
    "calendar_updated" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Availability" PRIMARY KEY (
        "listing_id"
     )
);

CREATE TABLE "Pricing" (
    "listing_id" INTEGER   NOT NULL,
    "price" NUMERIC   NOT NULL,
    "weekly_price" NUMERIC   NOT NULL,
    "monthly_price" NUMERIC   NOT NULL,
    "security_deposit" NUMERIC   NOT NULL,
    "cleaning_fee" NUMERIC   NOT NULL,
    "extra_people" NUMERIC   NOT NULL,
    "cancellation_policy" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Pricing" PRIMARY KEY (
        "listing_id"
     )
);

CREATE TABLE "Review_Statistics" (
    "listing_id" INTEGER   NOT NULL,
    "number_of_reviews" INTEGER   NOT NULL,
    "reviews_per_month" NUMERIC   NOT NULL,
    "first_review" DATE   NOT NULL,
    "last_review" DATE   NOT NULL,
    "review_scores_rating" INTEGER   NOT NULL,
    "review_scores_accuracy" INTEGER   NOT NULL,
    "review_scores_cleanliness" INTEGER   NOT NULL,
    "review_scores_checkin" INTEGER   NOT NULL,
    "review_scores_communication" INTEGER   NOT NULL,
    "review_scores_location" INTEGER   NOT NULL,
    "review_scores_value" INTEGER   NOT NULL,
    CONSTRAINT "pk_Review_Statistics" PRIMARY KEY (
        "listing_id"
     )
);

CREATE TABLE "Calendar" (
    "listing_id" INTEGER   NOT NULL,
    "date" DATE   NOT NULL,
    "available" BOOLEAN   NOT NULL,
    "price" NUMERIC   NOT NULL
);

CREATE TABLE "Reviews" (
    "review_id" INTEGER   NOT NULL,
    "listing_id" INTEGER   NOT NULL,
    "date" DATE   NOT NULL,
    "comments" VARCHAR   NOT NULL,
    "reviewer_id" INTEGER   NOT NULL,
    "reviewer_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Reviews" PRIMARY KEY (
        "review_id"
     )
);

ALTER TABLE "Property" ADD CONSTRAINT "fk_Property_host_id" FOREIGN KEY("host_id")
REFERENCES "Host" ("host_id");

ALTER TABLE "Host_Verifications" ADD CONSTRAINT "fk_Host_Verifications_host_id" FOREIGN KEY("host_id")
REFERENCES "Host" ("host_id");

ALTER TABLE "Address" ADD CONSTRAINT "fk_Address_listing_id" FOREIGN KEY("listing_id")
REFERENCES "Property" ("listing_id");

ALTER TABLE "Amenities" ADD CONSTRAINT "fk_Amenities_listing_id" FOREIGN KEY("listing_id")
REFERENCES "Property" ("listing_id");

ALTER TABLE "Availability" ADD CONSTRAINT "fk_Availability_listing_id" FOREIGN KEY("listing_id")
REFERENCES "Property" ("listing_id");

ALTER TABLE "Pricing" ADD CONSTRAINT "fk_Pricing_listing_id" FOREIGN KEY("listing_id")
REFERENCES "Property" ("listing_id");

ALTER TABLE "Review_Statistics" ADD CONSTRAINT "fk_Review_Statistics_listing_id" FOREIGN KEY("listing_id")
REFERENCES "Property" ("listing_id");

ALTER TABLE "Calendar" ADD CONSTRAINT "fk_Calendar_listing_id" FOREIGN KEY("listing_id")
REFERENCES "Property" ("listing_id");

ALTER TABLE "Reviews" ADD CONSTRAINT "fk_Reviews_listing_id" FOREIGN KEY("listing_id")
REFERENCES "Property" ("listing_id");

