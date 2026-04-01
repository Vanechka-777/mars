from flask import jsonify
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash
from data import db_session
from data.reqparse_job import parser  # парсер для job
from data.jobs import Job  # модель Job


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Job).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.get(Job, job_id)
        return jsonify({'job': job.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.get(Job, job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Job).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
            for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Job(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args.get('start_date'),  # если не указано, будет None
            end_date=args.get('end_date'),
            is_finished=args.get('is_finished', False)  # по умолчанию False
        )
        session.add(job)
        session.commit()
        return jsonify({'id': job.id})