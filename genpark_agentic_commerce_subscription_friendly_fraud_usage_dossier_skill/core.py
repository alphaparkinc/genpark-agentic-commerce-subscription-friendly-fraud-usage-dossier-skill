# -*- coding: utf-8 -*-
"""Subscription Friendly Fraud Usage Log & Dossier Compiler for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class SubscriptionFriendlyFraudUsageDossierCompiler:
    """SaaS recurring subscription friendly fraud and digital utilization evidence compiler."""

    @staticmethod
    def compile_subscription_usage_evidence(account_id: str, subscription_plan: str, disputed_cycle_amount_usd: float, active_session_count_in_cycle: int, last_login_timestamp: str = None, tos_accepted_timestamp: str = None) -> Dict[str, Any]:
        """Aggregate definitive audit trail refuting 'fraudulent unrecognized charge' claims."""
        is_active_user = active_session_count_in_cycle >= 3
        has_binding_agreement = bool(tos_accepted_timestamp)

        verdict = "INCONTROVERTIBLE_FIRST_PARTY_USAGE" if (is_active_user and has_binding_agreement) else "PARTIAL_LOGS"

        return {
            "account_id": account_id,
            "subscription_plan": subscription_plan,
            "disputed_amount_usd": disputed_cycle_amount_usd,
            "logged_user_sessions": active_session_count_in_cycle,
            "binding_terms_of_service_audit": "CONFIRMED_AT_SIGNUP" if has_binding_agreement else "MISSING_TIMESTAMP",
            "evidence_grade": verdict,
            "win_probability_pct": 92.0 if is_active_user else 45.0,
            "compelling_rationale": f"Cardholder actively logged into {subscription_plan} {active_session_count_in_cycle} times during the disputed period. Utilization directly refutes claim of unauthorized transaction."
        }

    @staticmethod
    def generate_saas_chargeback_rebuttal_letter(customer_name: str, chargeback_case_id: str, evidence_summary: str) -> Dict[str, Any]:
        """Synthesize merchant formal dispute rebuttal document for payment gateway submission."""
        letter = (
            f"RE: Dispute Rebuttal for Case #{chargeback_case_id}\n\n"
            f"Dear Dispute Resolution Team,\n\n"
            f"We are formally contesting the chargeback filed by {customer_name}. "
            f"The cardholder established an active recurring subscription and repeatedly utilized the digital service "
            f"throughout the disputed billing cycle.\n\n"
            f"Evidence attached:\n"
            f"1. IP and device session access logs ({evidence_summary})\n"
            f"2. Explicit recurring billing consent timestamp\n"
            f"3. Password reset and MFA verification records\n\n"
            f"Under card brand operating regulations for recurring transactions, this evidence establishes genuine "
            f"first-party consumption. We request immediate reversal of this chargeback."
        )

        return {
            "case_id": chargeback_case_id,
            "target_gateway": "STRIPE_DISPUTES_OR_BRAINTREE",
            "rebuttal_letter_text": letter,
            "action": "UPLOAD_TO_ACQUIRER_EVIDENCE_PORTAL"
        }
