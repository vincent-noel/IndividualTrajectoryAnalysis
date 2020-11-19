FROM colomoto/colomoto-docker:2020-08-01
MAINTAINER Vincent Noel <contact@vincent-noel.fr>

USER root

RUN mkdir -p /notebook/IndividualTrajectoryAnalysis/
COPY . /notebook/IndividualTrajectoryAnalysis/

RUN chown -R user:user /notebook/IndividualTrajectoryAnalysis
USER user
