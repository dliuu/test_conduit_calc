import datetime

class CreditMetricsCalculator:
    
    def __init__(self):
        pass

    def calc_tier(self, credit_score: int, experiences: int, foreign: bool) -> int:
        # Credit decision score
        if credit_score >= 750:
            score = 3
        elif credit_score >= 700:
            score = 2
        else:
            score = 0

        if foreign:
            score = 0 

        # Experience
        if experiences >= 20:
            score += 7
        elif experiences >= 10:
            score += 5
        elif experiences >= 3:
            score += 3
        else:
            score += 1

        return score

    def calc_metrics(self, program: str, purpose: str, score: int) -> dict:
        metrics = {"asis_ltv": 0,
                   "ltc": 0,
                   "ltvarv": 0}
        
        if program == "fix&flip":
            if purpose == 'purchase':
                if score >= 7:
                    metrics['asis_ltv'] = 0.9
                    metrics['ltc'] = 0.9
                    metrics['ltvarv'] = 0.75
                elif score >= 5:
                    metrics['asis_ltv'] = 0.85
                    metrics['ltc'] = 0.85
                    metrics['ltvarv'] = 0.70
                elif score >= 2:
                    metrics['asis_ltv'] = 0.825
                    metrics['ltc'] = 0.825
                    metrics['ltvarv'] = 0.65
                else:
                    metrics['asis_ltv'] = 0.75
                    metrics['ltc'] = 0.75
                    metrics['ltvarv'] = 0.60
            
            elif purpose == 'refinance_rate':
                if score >= 7:
                    metrics['asis_ltv'] = 0.75
                    metrics['ltc'] = None
                    metrics['ltvarv'] = 0.65
                elif score >= 5:
                    metrics['asis_ltv'] = 0.725
                    metrics['ltc'] = None
                    metrics['ltvarv'] = 0.65
                elif score >= 2:
                    metrics['asis_ltv'] = 0.7
                    metrics['ltc'] = None
                    metrics['ltvarv'] = 0.6
                else:
                    metrics['asis_ltv'] = 0.6
                    metrics['ltc'] = None
                    metrics['ltvarv'] = 0.55
            
            elif purpose == 'refinance_cashout':
                if score >= 7:
                    metrics['asis_ltv'] = 0.7
                    metrics['ltc'] = None
                    metrics['ltvarv'] = 0.65
                elif score >= 5:
                    metrics['asis_ltv'] = 0.675
                    metrics['ltc'] = None
                    metrics['ltvarv'] = 0.65
                elif score >= 2:
                    metrics['asis_ltv'] = 0.65
                    metrics['ltc'] = None
                    metrics['ltvarv'] = 0.6
                else:
                    metrics['asis_ltv'] = None
                    metrics['ltc'] = None
                    metrics['ltvarv'] = None
        
        return metrics
